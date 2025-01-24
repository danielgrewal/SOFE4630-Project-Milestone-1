# SOFE4630-Project-Milestone-1 Design Part: Producer-Consumer Model Using Google Cloud Pub/Sub

This contains the implementation of a producer-consumer model using Google Cloud Pub/Sub to process and handle data from a CSV file. The design demonstrates the use of Pub/Sub for real-time, scalable communication between distributed components.

## Overview

### Producer
- Reads data from the `Labels.csv` file.
- Converts each record into a serialized JSON message.
- Publishes messages to a Pub/Sub topic.

### Consumer
- Subscribes to the Pub/Sub topic.
- Retrieves and deserializes messages.
- Processes the data by printing the record values.

## Requirements

1. **Python**: Ensure Python 3.7+ is installed.
2. **Google Cloud SDK**: Required for managing Pub/Sub topics and subscriptions.
3. **Google Cloud Pub/Sub**:
   - Create a Pub/Sub topic (e.g., `csvRecordsTopic`) and subscription (e.g., `csvRecordsSubscription`) in your Google Cloud project.
   - Enable the Pub/Sub API for your project.
4. **Service Account Key**:
   - Obtain a valid Google Cloud Platform (GCP) JSON service account key.
   - Place the key in the same directory as the scripts.

## Installation and Dependencies

1. Clone this repository
2. Install Google Cloud Pub/Sub:
```pip install google-cloud-pubsub```

## Running The Scripts

1. Ensure the Labels.csv file is in the same directory as the producer script.
2. Run the producer script: ```python producer.py``` This script will read the CSV file and publish messages to the specified Pub/Sub topic.
3. Run the consumer script: ```python consumer.py``` The script will process and print the retrieved messages.


