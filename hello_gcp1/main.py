import os
import logging
import requests

from publish import publish_test


def hello_gcp1(request):

    req = requests.get('https://google.com')
    logging.info("Request status" + str(req.status_code))

    # Test env
    topic_name = os.environ.get("ACTIVITY_TOPIC", "No")

    # Test pub sub
    name = request.args.get('name')
    if name:
        publish_test(str(name))

    return str(topic_name)
