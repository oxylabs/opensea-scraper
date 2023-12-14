import requests
from pprint import pprint

# Structure payload.
payload = {
   'source': 'universal',
   'url': 'https://opensea.io/collection/the-10k-collection-pass/drop'
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('YOUR_USERNAME', 'YOUR_PASSWORD'), #Your credentials go here
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())
