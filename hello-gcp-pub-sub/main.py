from google.cloud.datastore import Client, Entity


def hello_gcp_pub_sub(event, context):
    data = event['attributes']['name']

    client = Client()

    pub_test_key = client.key('PubSubTest')
    pub_test = Entity(pub_test_key)
    pub_test['data'] = str(data)

    with client.transaction():
        client.put(pub_test)

    return "200"
