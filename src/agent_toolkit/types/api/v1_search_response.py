# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["V1SearchResponse", "Result"]


class Result(BaseModel):
    snippet: str
    """A clean summary or snippet from the search result"""

    title: str
    """The title of the search result"""

    url: str
    """The URL of the search result"""

    country: Optional[str] = None
    """Country context of this specific result if available"""

    crawl_date: Optional[date] = None
    """Date when the result was last crawled if available"""

    domain: Optional[str] = None
    """Domain of the result URL"""

    enhanced_with_selenium: Optional[bool] = None
    """Whether this result was enhanced with Selenium"""

    language: Optional[str] = None
    """Language of this specific result if available"""

    modified_date: Optional[date] = None
    """Last modification date of the result if available"""

    published_date: Optional[date] = None
    """Publication date of the result if available"""


class V1SearchResponse(BaseModel):
    query: str
    """The search query that was processed"""

    results: List[Result]
    """List of search results"""

    applied_filters: Optional[Dict[str, object]] = None
    """Filters that were applied to the search"""

    country: Optional[str] = None
    """Country used for the search"""

    enhanced_results_count: Optional[int] = None
    """Number of results that were enhanced with Selenium"""

    language: Optional[str] = None
    """Language used for the search"""

    result_count: Optional[int] = None
    """Number of results returned"""

    selenium_enhancement: Optional[bool] = None
    """Whether Selenium enhancement was enabled for this search"""

    summary: Optional[str] = None
    """Optional LLM-generated summary of results"""

    topic: Optional[str] = None
    """Search topic category used for the search"""
