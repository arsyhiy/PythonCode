import urllib.request

# URL of the bew page to fetch
url = "https://www.example.com"

try:
    # Open the URL and read its content
    response = urllib.request.urlopen(url)

    # Read the content of the response
    data = response.read()

    # Decode the data (if it's in bytes) to a string
    html_content = data.decode("utf-8")

    # Print the HtML content of the web page
    print(html_content)

except Exception as e:
    print("Error fetching URL:", e)
