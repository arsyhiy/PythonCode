import requests
from bs4  import BeautifulSoup
import json

is_scraping = True 
current_page = 1
scraped_data = []


while is_scraping:
    # Fetch the content from the URL 
    response = requests.get(f"https://news.ycombinator.com/?p={current_page}")
    html_content = response.content

    print(f"Scrapping page {current_page}: {response.url}")

    # Use BeautifulSoup to parse the HTML 
    soup = BeautifulSoup(html_content, "html.parser")
    articles = soup.find_all(class_="athing")


    # Check if articles are found 
    if articles is not None:
        for article in articles:
            data = {
                "URL": article.find(class_="titleline").find("a").get("href"),
                "title": article.find(class_="titleline").getText(),
                "rank": article.find(class_="rank").getText().replace(".", ""), 
            }
            scraped_data.append(data)

    # Check if there is a link to the next page 
    next_page_link = soup.find(class_="morelink")
        
    if next_page_link:
        current_page += 1
    else:
        is_scraping = False 
        print(f"Finished scraping! Total pages scraped: {current_page}")
        print(f"Total articles scraped: {len(scraped_data)}")


with open("hn_articles.json", "w", encoding="utf-8") as jsonfile:
    json.dump(scraped_data, jsonfile, indent=4)
