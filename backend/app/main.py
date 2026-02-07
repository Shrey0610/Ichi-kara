# main.py
"""
Entry point for the FastAPI backend application.
"""


from fastapi import FastAPI, Request
from pydantic import BaseModel

# Import fetch and extract functions from crawler module
from crawler.crawler import crawl_page


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
    return crawl_page(request.url)

