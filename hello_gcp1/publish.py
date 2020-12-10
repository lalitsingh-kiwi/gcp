""" File to create new comment. """
# Basic imports
import os

# Import PubSub
from google.cloud import pubsub

# Environment Variables
ACTIVITY_TOPIC = os.environ.get("ACTIVITY_TOPIC")

# Create Publisher Client
publisher = pubsub.PublisherClient()


def publish_test(data):
    publisher.publish(ACTIVITY_TOPIC, b'New Test', name=str(data))
