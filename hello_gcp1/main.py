import os
import requests

def hello_gcp1(request):
    # req = requests.get('https://google.com')
    # return str(req.status_code)
    # return "gcp1 test 103"
    db_user = os.environ.get("DB_USER", "")
    return str(db_user)
