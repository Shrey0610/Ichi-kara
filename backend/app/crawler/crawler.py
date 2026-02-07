# crawler.py
"""
Responsible for crawling web pages and gathering educational content.
Acts as a coordinator between fetch and extract modules.
"""

from .fetch import fetch_html
from .extract import extract_text


def crawl_page(url: str) -> dict:
    """
    Crawls a single web page and returns structured educational content.

    Args:
        url (str): URL of the page to crawl.

    Returns:
        dict: Crawled content including raw text.
    """
    html = fetch_html(url)

    # Basic guardrail for learning-stage robustness
    if html.startswith("Error:"):
        return {"url": url, "error": html}

    text = extract_text(html)

    return {
        "url": url,
        "content": text,
        "source_type": "web",
    }