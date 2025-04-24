# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ExtractResponse", "FailedResult", "Result"]


class FailedResult(BaseModel):
    error: str
    """Error message describing why the URL couldn't be processed."""

    url: str
    """The URL that failed to be processed."""


class Result(BaseModel):
    raw_content: str
    """The full content extracted from the page."""

    url: str
    """The URL from which content was extracted."""

    cache_hit: Optional[bool] = None
    """Indicates if this result was served from cache."""

    images: Optional[List[str]] = None
    """List of image URLs extracted from the page."""

    links: Optional[List[str]] = None
    """List of internal links found on the page."""


class ExtractResponse(BaseModel):
    response_time: float
    """Time in seconds it took to complete the request."""

    failed_results: Optional[List[FailedResult]] = None
    """List of failed extractions."""

    results: Optional[List[Result]] = None
    """List of successful extractions."""
