import requests
from bs4 import BeautifulSoup
import os

# Function to fetch articles from a given URL and save them as text files
def fetch_articles(url, save_dir):
    """
    Fetches articles from the specified URL and saves them in the specified directory.

    Args:
        url (str): The URL of the website to fetch articles from.
        save_dir (str): The directory where the articles will be saved.

    Returns:
        None
    """
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch articles. Status code: {response.status_code}")
        return

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all articles on the webpage (adjust selector as needed)
    articles = soup.find_all("article")
    if not articles:
        print("No articles found on the webpage.")
        return

    # Create the directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Iterate over each article and save its content
    for i, article in enumerate(articles):
        # Extract the title (adjust the selector as needed)
        title_element = article.find("h2")
        title = title_element.get_text(strip=True) if title_element else f"article_{i+1}"

        # Extract the content (adjust the selector as needed)
        content_element = article.find("p")
        content = content_element.get_text(strip=True) if content_element else "No content available."

        # Save the article to a text file
        filename = os.path.join(save_dir, f"{title.replace(' ', '_')}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"{title}\n\n{content}")

        print(f"Saved: {filename}")

# Main block for running the script
def main():
    """
    Main function to fetch articles from a URL and save them to a directory.
    """
    # URL of the website to fetch articles from (adjust as needed)
    url = "https://example-news-website.com"

    # Directory to save the articles
    save_dir = "data/raw/"

    # Call the fetch_articles function
    fetch_articles(url, save_dir)

if __name__ == "__main__":
    main()
