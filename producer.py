from google.cloud import pubsub_v1
import csv
import glob
import json
import os

# Search for the JSON service account key
files = glob.glob("*.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = files[0]

# Set the project ID and topic name
project_id = "sofe4630"
topic_name = "csvRecords"

# Create a publisher and define the topic path
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)
print(f"Publishing messages to {topic_path}.")

# Open the CSV file and read the records
with open("Labels.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Convert each row to a JSON string
        message = json.dumps(row).encode("utf-8")
        print(f"Producing a record: {row}")
        
        # Publish the serialized message to the topic
        future = publisher.publish(topic_path, message)
        # Ensure the message is succesfully published
        future.result()

print("All messages published successfully.")
