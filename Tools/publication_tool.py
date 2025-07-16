from crewai.tools import tool
import urllib.request
from urllib.parse import quote
import xml.etree.ElementTree as ET

@tool("publication_fetching_tool")
def fetch_publications(argument: str) -> list:
    """Fetches titles of publications from arXiv based on a search query."""
    print("running publication tool")
    print(f"[DEBUG] Tool input: {argument}")
    query = quote(argument)
    url = f"https://export.arxiv.org/api/query?search_query=all:{query}&max_results=5"
    
    try:
        data = urllib.request.urlopen(url).read().decode("utf-8")
    except Exception as e:
        return f"[ERROR] Failed to fetch publications: {e}"

    root = ET.fromstring(data)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    titles = []
    for entry in root.findall("atom:entry", ns):
        title = entry.find("atom:title", ns)
        if title is not None:
            titles.append(title.text.strip())

    if not titles:
        return "No publications found."
    return titles

# if __name__ == "__main__":
#     print(fetch_publications('ResNet performs worse than Vgg16'))
