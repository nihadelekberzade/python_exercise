import requests
from bs4 import BeautifulSoup

# URL of the article
url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
        # Find the element that contains the article text
    article_element = soup.find("div")
    print(type(article_element))

    # Extract and print the text of the article
    if article_element:
        article_text = article_element.get_text()
        print(article_text)
    else:
        print("Article content not found on the page.")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
