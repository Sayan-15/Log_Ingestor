import requests
import json
from datetime import datetime

log_data = {
    "level": "Error",
    "message": "Database Not Found",
    "resourceId": "server-1234",
    "timestamp": datetime.utcnow().isoformat(),
    "traceId": "abc-xyz-1234",
    "spanId": "span-1234",
    "commit": "5e54562f",
    "metadata": {
        "parentResourceId": "server-0456"
    }
}

ingestor_url = 'http://localhost:3000/ingest'

response = requests.post(ingestor_url, json=log_data)

if response.status_code == 200:
    print('Log ingested successfully.')
else:
    print('Failed to ingest log. Status code:', response.status_code)
    print(response.text)
