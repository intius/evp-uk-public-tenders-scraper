# UK public tenders Scraper & Unofficial API (Python, Node.js, MCP)

[Run UK Public Tenders Scraper - Find a Tender & Contracts Finder on Apify](https://apify.com/evpp/uk-public-tenders) to export UK public tenders data as clean JSON, CSV, Excel, or an API feed. This repository is a developer quick-start kit with working Python and Node.js clients, an MCP configuration, a real sample dataset, and an n8n automation template.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-orange)](https://apify.com/evpp/uk-public-tenders)

[Open the documentation and crawlable sample explorer](https://intius.github.io/evp-labs-data-extractors/actors/uk-public-tenders/) for quick inputs, integration links, real sample rows, and ready-made task examples.

## Why use this UK public tenders scraper?

- Export UK public tenders data without building or maintaining a custom scraper
- Get flat, schema documented JSON ready for analytics, lead generation, market research, and AI agents
- Run manually, on a schedule, through the Apify API, or through MCP compatible AI tools
- Use the included 25+ row sample dataset to prototype before running the live Actor

Built for B2G vendors bidding on UK public contracts, bid consultancies, tender-alert services, export agencies.

## Quick start on Apify

Open [https://apify.com/evpp/uk-public-tenders](https://apify.com/evpp/uk-public-tenders) and use this input:

```json
{
  "updatedSince": "2026-10-24",
  "updatedUntil": "",
  "publishedSince": "",
  "keyword": "",
  "noticeTypes": "any",
  "maxItems": 10
}
```

## Python

```bash
pip install -r requirements.txt
export APIFY_TOKEN=your_apify_token
python python/run.py
```

On Windows PowerShell, use `$env:APIFY_TOKEN="your_apify_token"` instead of `export`.

## Node.js

```bash
npm install
export APIFY_TOKEN=your_apify_token
node node/run.mjs
```

## MCP and AI agents

Add the hosted Apify MCP server from `mcp-config.json` to your MCP client:

```json
{
  "mcpServers": {
    "apify": {
      "type": "http",
      "url": "https://mcp.apify.com/?tools=evpp/uk-public-tenders"
    }
  }
}
```

Then ask your agent to run `evpp/uk-public-tenders`, inspect the output schema, or export the latest dataset. The direct MCP URL is `https://mcp.apify.com/?tools=evpp/uk-public-tenders`.

For multi-source public data agents, use the [EVP Public Data MCP server](https://github.com/intius/evp-public-data-mcp). It is published in the Official MCP Registry as `io.github.intius/evp-public-data-mcp` and is also available as a one-click Claude Desktop MCPB release.

## n8n automation

Import `n8n-workflow.json` into n8n, select your Apify credential, replace the webhook placeholder, and activate the schedule. The workflow runs the Actor every morning and posts fresh dataset items to your webhook.

## Output schema

| Field | Type | Description |
|---|---|---|
| `ocid` | string | OCDS open contracting ID shared across all releases of one procurement |
| `releaseId` | string | Find a Tender release / notice ID |
| `releaseDate` | string | When this release was published (ISO 8601) |
| `tag` | string[] | OCDS release tags (tender, award, contract, planning) |
| `noticeType` | string | Find a Tender notice type code (UK3 planning, UK4 tender, UK5 award, UK7 contract details) |
| `noticeUrl` | string | Public notice page on Find a Tender |
| `tenderTitle` | string | Tender / contract title |
| `tenderDescription` | string | Tender description trimmed to ~500 characters |
| `tenderStatus` | string | OCDS tender status (active, complete, cancelled, ...) |
| `procurementMethod` | string | OCDS procurement method (open, selective, limited, direct) |
| `category` | string | Main procurement category (works, services, goods) |
| `cpvCodes` | string[] | CPV classification codes across tender and award items |
| `buyerName` | string | Contracting authority / buyer name |
| `buyerId` | string | Buyer identifier (usually a GB-PPON organisation ID) |
| `region` | string | UK NUTS/ITL region code of the buyer or delivery address |
| `value` | number | Estimated tender value (ex VAT) |
| `currency` | string | Value currency code |
| `tenderDeadline` | string | End of the tender submission period (ISO 8601) |
| `enquiryDeadline` | string | End of the enquiry period (ISO 8601) |
| `awardDate` | string | Award date or contract signature date (ISO 8601) |
| `awardValue` | number | Awarded contract value (ex VAT) |
| `suppliers` | string[] | Winning supplier names on award notices |

## Real sample output

The first sanitized row from the included sample dataset:

```json
{
  "ocid": "ocds-h6vhtk-03b792",
  "releaseId": "112310-2026",
  "releaseDate": "2026-11-26T16:54:33Z",
  "tag": [
    "award",
    "contract"
  ],
  "noticeUrl": "https://www.find-tender.service.gov.uk/Notice/112310-2026",
  "tenderTitle": "Dynamic Purchasing System For Passenger Transport Services 2023",
  "tenderDescription": "A mini competition was carried out under Lot 1 of the Aberdeenshire Council Dynamic Purchasing System 2023-2028 for the provision of Mainstream School transport services.",
  "tenderStatus": "complete",
  "procurementMethod": "selective",
  "category": "services",
  "cpvCodes": [
    "60000000",
    "60100000",
    "60112000",
    "60130000",
    "60140000",
    "60170000",
    "60120000",
    "60171000",
    "60172000"
  ],
  "buyerName": "Aberdeenshire Council",
  "buyerId": "GB-FTS-756",
  "region": "UKM50",
  "awardDate": "2026-10-15T00:00:00+01:00",
  "awardValue": 722820.34,
  "suppliers": [
    "Central Taxis (North East) Limited",
    "Victoria Group Limited",
    "Whytes Coaches Ltd",
    "RS Coaches",
    "A&I Coaches Ltd"
  ]
}
```

## Files in this kit

| File | Purpose |
|---|---|
| `python/run.py` | Working Python Apify API example |
| `node/run.mjs` | Working Node.js Apify API example |
| `mcp-config.json` | MCP server configuration for AI agents |
| `sample-output.json` | First five sanitized sample rows |
| `dataset-snapshot.csv` | 25+ row evaluation snapshot |
| `DATASET_CARD.md` | Dataset documentation and provenance |
| `n8n-workflow.json` | Scheduled n8n automation template |

## Fresh data

This repository contains a static evaluation sample. For current data, run the live Actor: https://apify.com/evpp/uk-public-tenders

## Responsible use

The Actor reads public data from `find-tender.service.gov.uk`. Review the source site's terms and applicable privacy rules before production use.
