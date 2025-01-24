from google.cloud import pubsub_v1
import glob
import json
import os

# Search for the JSON service account key
files = glob.glob("*.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = files[0]

# Set the project ID and subscription name
project_id = "sofe4630"
subscription_id = "csvRecords-sub"

# Create a subscriber and define the subscription path
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)
print(f"Listening for messages on {subscription_path}...")

# Callback function to handle received messages
def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    # Deserialize the received message and acknowledge it was received
    record = json.loads(message.data.decode("utf-8"))
    print(f"Consumed record: {record}")
    message.ack()

# Start the subscriber to listen for messages and pull them
with subscriber:
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    try:
        streaming_pull_future.result()
    except KeyboardInterrupt:
        streaming_pull_future.cancel()
        print("\nStopped listening for messages.")
