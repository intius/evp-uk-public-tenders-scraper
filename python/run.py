import json
import os
from apify_client import ApifyClient

APIFY_TOKEN = os.environ.get("APIFY_TOKEN")
if not APIFY_TOKEN:
    raise SystemExit("Set APIFY_TOKEN before running this example.")

client = ApifyClient(APIFY_TOKEN)
run_input = json.loads('''{"updatedSince":"2026-10-24","updatedUntil":"","publishedSince":"","keyword":"","noticeTypes":"any","maxItems":10}''')
run = client.actor("evpp/uk-public-tenders").call(run_input=run_input)
items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(json.dumps(items[:5], indent=2, ensure_ascii=False))
print(f"Fetched {len(items)} items. Open the full dataset: https://console.apify.com/storage/datasets/{run['defaultDatasetId']}")
