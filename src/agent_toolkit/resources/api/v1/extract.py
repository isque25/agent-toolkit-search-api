# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.api.v1 import extract_create_params, extract_retrieve_params
from ....types.api.v1.extract_response import ExtractResponse

__all__ = ["ExtractResource", "AsyncExtractResource"]


class ExtractResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/agent-toolkit-python#accessing-raw-response-data-eg-headers
        """
        return ExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/agent-toolkit-python#with_streaming_response
        """
        return ExtractResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        urls: List[str],
        extract_depth: Literal["basic", "advanced"] | NotGiven = NOT_GIVEN,
        include_images: bool | NotGiven = NOT_GIVEN,
        include_links: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractResponse:
        """
        Extract content from one or more URLs using Selenium.

        Args: request: ExtractRequest object with URLs and extraction options

        Returns: ExtractResponse with extraction results and metadata

        Args:
          urls: List of URLs to extract content from.

          extract_depth: Depth of extraction. 'advanced' retrieves more data including tables and
              embedded content.

          include_images: Include images in the response.

          include_links: Include internal links found on the page in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/extract",
            body=maybe_transform(
                {
                    "urls": urls,
                    "extract_depth": extract_depth,
                    "include_images": include_images,
                    "include_links": include_links,
                },
                extract_create_params.ExtractCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    def retrieve(
        self,
        *,
        url: str,
        extract_depth: str | NotGiven = NOT_GIVEN,
        include_images: bool | NotGiven = NOT_GIVEN,
        include_links: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractResponse:
        """
        Extract content from a URL using Selenium (GET method).

        Args: url: URL to extract content from include_images: Whether to include images
        in the result include_links: Whether to include internal links in the result
        extract_depth: Depth of extraction ("basic" or "advanced")

        Returns: ExtractResponse with extraction results and metadata

        Args:
          url: URL to extract content from

          extract_depth: Depth of extraction ('basic' or 'advanced')

          include_images: Include images in the response

          include_links: Include internal links found on the page in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/extract",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "extract_depth": extract_depth,
                        "include_images": include_images,
                        "include_links": include_links,
                    },
                    extract_retrieve_params.ExtractRetrieveParams,
                ),
            ),
            cast_to=ExtractResponse,
        )


class AsyncExtractResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/agent-toolkit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/agent-toolkit-python#with_streaming_response
        """
        return AsyncExtractResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        urls: List[str],
        extract_depth: Literal["basic", "advanced"] | NotGiven = NOT_GIVEN,
        include_images: bool | NotGiven = NOT_GIVEN,
        include_links: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractResponse:
        """
        Extract content from one or more URLs using Selenium.

        Args: request: ExtractRequest object with URLs and extraction options

        Returns: ExtractResponse with extraction results and metadata

        Args:
          urls: List of URLs to extract content from.

          extract_depth: Depth of extraction. 'advanced' retrieves more data including tables and
              embedded content.

          include_images: Include images in the response.

          include_links: Include internal links found on the page in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/extract",
            body=await async_maybe_transform(
                {
                    "urls": urls,
                    "extract_depth": extract_depth,
                    "include_images": include_images,
                    "include_links": include_links,
                },
                extract_create_params.ExtractCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    async def retrieve(
        self,
        *,
        url: str,
        extract_depth: str | NotGiven = NOT_GIVEN,
        include_images: bool | NotGiven = NOT_GIVEN,
        include_links: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractResponse:
        """
        Extract content from a URL using Selenium (GET method).

        Args: url: URL to extract content from include_images: Whether to include images
        in the result include_links: Whether to include internal links in the result
        extract_depth: Depth of extraction ("basic" or "advanced")

        Returns: ExtractResponse with extraction results and metadata

        Args:
          url: URL to extract content from

          extract_depth: Depth of extraction ('basic' or 'advanced')

          include_images: Include images in the response

          include_links: Include internal links found on the page in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/extract",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "extract_depth": extract_depth,
                        "include_images": include_images,
                        "include_links": include_links,
                    },
                    extract_retrieve_params.ExtractRetrieveParams,
                ),
            ),
            cast_to=ExtractResponse,
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.create = to_raw_response_wrapper(
            extract.create,
        )
        self.retrieve = to_raw_response_wrapper(
            extract.retrieve,
        )


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.create = async_to_raw_response_wrapper(
            extract.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            extract.retrieve,
        )


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.create = to_streamed_response_wrapper(
            extract.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            extract.retrieve,
        )


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.create = async_to_streamed_response_wrapper(
            extract.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            extract.retrieve,
        )
