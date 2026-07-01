# Custom WebBrowser — Wikipedia Search Engine

A simple Python command-line tool that searches Wikipedia and saves your search history to a local JSON file. Built as a learning project to explore working with web APIs in Python.

## Features

- 🔍 Search Wikipedia directly from the terminal
- 📄 Returns the top 5 matching article titles and URLs
- 💾 Automatically saves every search (query, timestamp, and results) to `results.json`
- 📈 Keeps a running history across multiple searches — nothing gets overwritten
- 🆓 Completely free to use — no API key, no signup, no rate-limit worries for personal use

## Tech Stack

- Python 3.9+ (tested on 3.14.6)
- [`requests`](https://pypi.org/project/requests/) — for calling the Wikipedia API
- Wikipedia's free [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page)

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/VandanGupte/Custom-WebBrowser-using-exa-api-.git
   cd Custom-WebBrowser-using-exa-api-
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install requests
   ```

## Usage

Run the script:
```bash
python3 main.py
```

You'll be prompted to enter a search term:
```
Search here: fifa world cup 2026
```

The script prints the top 5 matching Wikipedia articles:
```
Title: 2026 FIFA World Cup
URL: https://en.wikipedia.org/wiki/2026_FIFA_World_Cup
...
```

Every search is also appended to `results.json`, so you build up a searchable history over time.

## Example `results.json` entry

```json
[
  {
    "query": "fifa world cup 2026",
    "timestamp": "2026-07-01T14:40:12.123456",
    "results": [
      {
        "title": "2026 FIFA World Cup",
        "url": "https://en.wikipedia.org/wiki/2026_FIFA_World_Cup"
      }
    ]
  }
]
```

## Project Structure

```
.
├── main.py         # Main script — search + save logic
├── results.json    # Auto-generated search history (created on first run)
├── requirements.txt
└── README.md
```

## Notes

- This project originally used the [Exa API](https://exa.ai) for semantic search, but was switched to Wikipedia's free public API to avoid any API keys, credits, or billing.
- `results.json` is excluded from version control via `.gitignore` by default, since it contains personal search history. Remove it from `.gitignore` if you'd like to track it.

