import requests

from virtualqueue_sdk.config import API_BASE_PATH

QUEUES_API_URL = f"{API_BASE_PATH}queue/"


def verify_finished_line(token: str):
    response = requests.get(f"{QUEUES_API_URL}verify?token={token}")
    print(response)
