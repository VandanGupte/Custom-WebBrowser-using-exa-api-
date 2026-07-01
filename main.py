import json
import os
from datetime import datetime
from exa_py import Exa

exa = Exa(api_key="Enter your API key here")

query = input("Search here: ")

response = exa.search(
    query,
    num_results=5,
    type="keyword",
    include_domains=["wikipedia.org"],
)

new_results = [
    {"title": result.title, "url": result.url}
    for result in response.results
]

for item in new_results:
    print(f"Title: {item['title']}")
    print(f"URL: {item['url']}")
    print()


filename = "results.json"
if os.path.exists(filename):
    with open(filename, "r") as f:
        history = json.load(f)
else:
    history = []


history.append({
    "query": query,
    "timestamp": datetime.now().isoformat(),
    "results": new_results,
})


with open(filename, "w") as f:
    json.dump(history, f, indent=2)

print(f"Saved search to {filename} (total searches so far: {len(history)})")