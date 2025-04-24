# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1SearchParams"]


class V1SearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query string"""

    country: Optional[str]
    """Country code (e.g., 'us', 'gb')"""

    crawl_end_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """End date for crawled content (YYYY-MM-DD)"""

    crawl_start_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Start date for crawled content (YYYY-MM-DD)"""

    exclude_domains: Optional[List[str]]
    """Domains to exclude from search results"""

    exclude_terms: Optional[List[str]]
    """Terms that must be excluded from search results"""

    include_domains: Optional[List[str]]
    """Domains to include in search results"""

    include_terms: Optional[List[str]]
    """Terms that must be included in search results"""

    language: Optional[str]
    """ISO language code (e.g., 'en', 'fr')"""

    max_results: int
    """Maximum number of results to return"""

    provider: Optional[Literal["google", "bing", "duckduckgo"]]
    """Search provider to use"""

    published_end_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """End date for published content (YYYY-MM-DD)"""

    published_start_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Start date for published content (YYYY-MM-DD)"""

    summarize: bool
    """Whether to generate a summary of results using LLM"""

    topic: Literal["general", "news", "images", "videos", "finance"]
    """Search topic category"""

    use_selenium: bool
    """
    Whether to enhance DuckDuckGo results with Selenium (only applies to DuckDuckGo
    provider)
    """
