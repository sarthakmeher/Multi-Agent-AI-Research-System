from langchain.tools import tool  #decorator
import requests  #scrappping
from bs4 import BeautifulSoup  #scrappping
from tavily import TavilyClient  #tavily api
import os #environment variables
from dotenv import load_dotenv #environment variables
from rich import print  #for colorful printing
load_dotenv()


tavily = TavilyClient(api_key = os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """
    This tool allows you to perform a web search using the Tavily API.
    You can use this tool to find information on the internet based on a query.
    Returns Titles, URLs and Snippets of the search results.
    """
    results = tavily.search(query = query, max_results = 5)
   
    out = []
    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    return "\n-----\n".join(out)    

print(web_search.invoke("What is the recent news of war?"))
        
        
        
@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
    
scrape_url.invoke("https://www.nbcnews.com/world/iran-war")