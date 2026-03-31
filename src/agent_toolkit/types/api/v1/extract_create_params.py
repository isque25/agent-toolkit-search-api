# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ExtractCreateParams"]


class ExtractCreateParams(TypedDict, total=False):
    urls: Required[SequenceNotStr[str]]
    """List of URLs to extract content from."""

    extract_depth: Literal["basic", "advanced"]
    """Depth of extraction.

    'advanced' retrieves more data including tables and embedded content.
    """

    include_images: bool
    """Include images in the response."""

    include_links: bool
    """Include internal links found on the page in the response."""
