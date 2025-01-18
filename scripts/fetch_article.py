import requests
from bs4 import BeautifulSoup

def fetch_article_from_url(url):
    """
    Fetch the text content of an article from the specified URL.
    
    Args:
        url (str): The URL of the article.
    
    Returns:
        str: The extracted article content.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch the article. Status code: {response.status_code}")
    
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    content = "\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])
    
    if not content:
        raise ValueError("No content found in the specified URL.")
    
    return content
