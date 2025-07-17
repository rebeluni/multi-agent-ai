import os
import requests
from dotenv import load_dotenv
load_dotenv()

def log_to_slack(content):
    url = os.getenv("SLACK_WEBHOOK_URL")
    data = {"text": content}
    response = requests.post(url, json=data)
    return response.status_code
