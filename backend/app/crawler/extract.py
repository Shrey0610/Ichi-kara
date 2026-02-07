# extract.py
"""
Extracts readable article text from raw HTML using BeautifulSoup.
This file is written for learning purposes and demonstrates basic HTML parsing.
"""

from bs4 import BeautifulSoup


def extract_text(html):
    """
    Accepts raw HTML as input, removes script and style tags, and returns clean plain text.
    Args:
        html (str): The raw HTML content to process.
    Returns:
        str: The cleaned, readable article text.
    """
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Remove all script and style elements
    for tag in soup(['script', 'style']):
        tag.decompose()  # Completely remove the tag from the soup

    # Get the text from the HTML
    text = soup.get_text()

    # Break lines and remove extra whitespace
    lines = (line.strip() for line in text.splitlines())
    # Remove empty lines
    clean_text = '\n'.join(line for line in lines if line)

    return clean_text
