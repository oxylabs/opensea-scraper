# OpenSea Scraper

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

With [OpenSea Scraper](https://oxylabs.io/products/scraper-api/web/opensea), you can extract NFT collections, items, prices, images, sales volumes, and more from the leading NFT marketplace on a large scale and block-free

Follow this guide to scrape OpenSea using our [Scraper API](https://oxylabs.io/products/scraper-api). 

### How it works

You can receive OpenSea results by providing URLs to our service. The API returns an HTML of any Expedia page.

#### Python code example

The example below shows how to get the result from an OpenSea page in HTML format.

```python
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
```

Code samples for other programming languages are [here](https://github.com/oxylabs/opensea-scraper/tree/main/code%20examples), and Oxylabs documentation is [here](https://developers.oxylabs.io/scraper-apis/web-scraper-api).

#### Output example

```json
{
    "results": [
        {
            "content":"<!doctype html>\n<html lang=\"en\">\n<head>...</script></body>\n</html>\n",
            "created_at": "2023-07-03 15:44:26",
            "updated_at": "2023-07-03 15:44:33",
            "page": 1,
            "url": "https://opensea.io/collection/the-10k-collection-pass/drop",
            "job_id": "7081658957328044033",
            "status_code": 200
        }
    ]
}
```

Utilize Oxylabs' OpenSea Scraper to delegate infrastructure management and web unblocking to us, enabling you to focus on the critical elements, namely, data and its analysis.

Should you have any inquiries, feel free to reach out to us at hello@oxylabs.io or engage in live chat through our website.
