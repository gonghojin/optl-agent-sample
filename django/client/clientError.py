import os
from dotenv import load_dotenv
import time
from sys import argv

from requests import get

serverIp = os.getenv('PYTHON_DEMO_SERVER_ENDPOINT', 'http://localhost:8002')
load_dotenv()

def polls():
    headers = {}
    requested = get(
        serverIp + "/polls",
        params={"param": argv[1]},
        headers=headers,
        )

    assert requested.status_code == 200
    print(requested)


def pollsError():
    headers = {}
    requested = get(
        serverIp + "/polls/error",
        params={"param": argv[1]},
        headers=headers,
    )

    assert requested.status_code == 500
    print(requested)

def pollsSqlite():
    headers = {}
    requested = get(
        serverIp + "/polls/error-sqlite",
        # params={"param": argv[1]},
        headers=headers,
        )
    assert requested.status_code == 500
    print(requested)

while 1:
    polls()
    pollsSqlite()
    pollsError()
    time.sleep(int(os.getenv("timeSleep")))