# OpenSea Scraper

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/product-integrations/refs/heads/master/Affiliate-Universal-1090x275.png)](https://oxylabs.io/pages/gitoxy?utm_source=877&utm_medium=affiliate&groupid=877&utm_content=opensea-scraper-github&transaction_id=102f49063ab94276ae8f116d224b67)

<p align="left">
  <a href="https://dashboard.oxylabs.io"><img src="https://img.shields.io/badge/%F0%9F%9A%80_Get_Started-FF6B35?style=for-the-badge" alt="Get started"></a>
  <a href="https://developers.oxylabs.io/products/web-api"><img src="https://img.shields.io/badge/%F0%9F%93%9A_Documentation-4A90E2?style=for-the-badge" alt="Documentation"></a>
  <a href="https://dashboard.oxylabs.io"><img src="https://img.shields.io/badge/%F0%9F%93%8A_Dashboard-2EA44F?style=for-the-badge" alt="Dashboard"></a>
  <a href="https://discord.gg/Pds3gBmKMH"><img src="https://img.shields.io/badge/%F0%9F%92%AC_Discord-5865F2?style=for-the-badge" alt="Discord"></a>
  <a href="https://www.youtube.com/@oxylabs"><img src="https://img.shields.io/badge/%E2%96%B6%EF%B8%8F_YouTube-FF0000?style=for-the-badge" alt="YouTube"></a>
</p>

With [OpenSea Scraper](https://oxylabs.io/products/scraper-api/web/opensea), you can extract NFT collections, items, prices, images, sales volumes, and more from the leading NFT marketplace on a large scale and block-free.

Follow this guide to scrape OpenSea using our [Scraper API](https://oxylabs.io/products/scraper-api). 

### How it works

You can receive OpenSea results by providing URLs to our service. The API returns an HTML of any OpenSea page.

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

Code samples for other programming languages are [here](https://github.com/oxylabs/opensea-scraper/tree/main/code%20examples), and Oxylabs documentation is [here](https://developers.oxylabs.io/products/web-scraper-api).

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

Should you have any inquiries, feel free to reach out to us at support@oxylabs.io or engage in live chat through our website.
