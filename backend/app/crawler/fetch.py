# fetch.py
"""
Fetches the HTML content from a given URL using the requests library.
This file is written for learning purposes and demonstrates basic web fetching.
"""

import requests


def fetch_html(url):
    """
    Takes a URL as input, fetches the HTML content, and returns it as raw text.
    Args:
        url (str): The web address to fetch.
    Returns:
        str: The raw HTML content of the page.
    """
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the raw HTML content as text
        return response.text
    else:
        # If the request failed, return an error message
        return f"Error: Unable to fetch page (status code: {response.status_code})"
