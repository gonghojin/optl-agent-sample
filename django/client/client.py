import os
import time
from sys import argv

from requests import get

serverIp = os.getenv('PYTHON_DEMO_SERVER_ENDPOINT', 'http://localhost:8000/polls')

while 1:
    headers = {}
    requested = get(
        serverIp + "/polls",
        params={"param": argv[1]},
        headers=headers,
    )

    assert requested.status_code == 200
    print(requested)
    time.sleep(10)

