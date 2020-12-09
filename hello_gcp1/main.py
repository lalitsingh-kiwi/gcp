import requests

def hello_gcp1(request):
    req = requests.get('https://google.com')
    return req.status_code
    # return "gcp1 test 103"
