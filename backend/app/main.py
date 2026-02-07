# main.py
"""
Entry point for the FastAPI backend application.
"""


from fastapi import FastAPI, Request
from pydantic import BaseModel

# Import fetch and extract functions from crawler module
from crawler.fetch import fetch_html
from crawler.extract import extract_text

# Create FastAPI app instance
app = FastAPI()

# Define a Pydantic model for the request body
class CrawlRequest(BaseModel):
    url: str

# FastAPI routing: @app.get, @app.post, etc. decorators define endpoints
@app.get("/")
def read_root():
    """
    Root endpoint. Returns a welcome message.
    """
    return {"message": "Welcome to ichi-kara backend!"}

@app.post("/crawl")
def crawl_url(request: CrawlRequest):
    """
    POST endpoint to crawl a URL and return extracted clean text.
    """
    # Fetch raw HTML from the given URL
    html = fetch_html(request.url)
    # Extract clean text from the HTML
    clean_text = extract_text(html)
    # Return the result as JSON
    return {"text": clean_text}
