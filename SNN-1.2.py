

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    # URL of the page you want to scrape
    url = 'https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2019.csv'

    # Send a GET request to the page
    response = requests.get(url)
    response.raise_for_status()  # Make sure the request was successful

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    #
    # Find the parent <div> by some identifying feature, e.g., an id
    parent_div = soup.find('<div>1<div>')

    # Get all children of the parent <div> that are tags
    child_divs = [child for child in parent_div.children if child.name is not None]

    # Extract the text from each child <div> and store it in a list
    children_text = [child.text for child in child_divs]