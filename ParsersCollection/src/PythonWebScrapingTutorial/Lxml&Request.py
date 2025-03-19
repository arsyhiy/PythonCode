from lxml import html
import requests

# Define the URL of the website to scrape
url = "https://example.com"

# Send an HTTP request to the website and retrive the HTML content
response = requests.get(url)

# Parse the HTML content using lxml
tree = html.fromstring(response.content)

# Extract specific elements from the HTML tree using XPath
# For example, let's extract the title of all the links on the page
links_titles = tree.xpath("//a/text()")

# Print the extracted link titles
for title in links_titles:
    print(title)
