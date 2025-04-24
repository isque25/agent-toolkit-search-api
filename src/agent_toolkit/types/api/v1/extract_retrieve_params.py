# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExtractRetrieveParams"]


class ExtractRetrieveParams(TypedDict, total=False):
    url: Required[str]
    """URL to extract content from"""

    extract_depth: str
    """Depth of extraction ('basic' or 'advanced')"""

    include_images: bool
    """Include images in the response"""

    include_links: bool
    """Include internal links found on the page in the response"""
