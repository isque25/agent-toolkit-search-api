# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from .extract import (
    ExtractResource,
    AsyncExtractResource,
    ExtractResourceWithRawResponse,
    AsyncExtractResourceWithRawResponse,
    ExtractResourceWithStreamingResponse,
    AsyncExtractResourceWithStreamingResponse,
)
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
from ....types.api import v1_search_params
from ...._base_client import make_request_options
from ....types.api.v1_search_response import V1SearchResponse
from ....types.api.v1_get_credits_response import V1GetCreditsResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def extract(self) -> ExtractResource:
        return ExtractResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/agent-toolkit-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/agent-toolkit-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def get_credits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetCreditsResponse:
        """
        Get current credit usage and limits for the authenticated user.

        Returns: CreditResponse with total, used, and remaining credits
        """
        return self._get(
            "/api/v1/credits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetCreditsResponse,
        )

    def search(
        self,
        *,
        query: str,
        country: Optional[str] | NotGiven = NOT_GIVEN,
        crawl_end_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        crawl_start_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        exclude_domains: Optional[List[str]] | NotGiven = NOT_GIVEN,
        exclude_terms: Optional[List[str]] | NotGiven = NOT_GIVEN,
        include_domains: Optional[List[str]] | NotGiven = NOT_GIVEN,
        include_terms: Optional[List[str]] | NotGiven = NOT_GIVEN,
        language: Optional[str] | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        provider: Optional[Literal["google", "bing", "duckduckgo"]] | NotGiven = NOT_GIVEN,
        published_end_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        published_start_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        summarize: bool | NotGiven = NOT_GIVEN,
        topic: Literal["general", "news", "images", "videos", "finance"] | NotGiven = NOT_GIVEN,
        use_selenium: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1SearchResponse:
        """
        Search endpoint that returns formatted results from external search provider.

        Args: query: The search query string language: Optional ISO language code (e.g.,
        'en', 'fr') country: Optional country code (e.g., 'us', 'gb') max_results:
        Maximum number of results to return (1-10) summarize: Whether to generate a
        summary of results using LLM provider: Search provider to use (google, bing,
        duckduckgo) topic: Search topic category use_selenium: Whether to enhance
        DuckDuckGo results with Selenium published_start_date: Filter results published
        after this date published_end_date: Filter results published before this date
        crawl_start_date: Filter results crawled after this date crawl_end_date: Filter
        results crawled before this date include_domains: Filter results to only include
        these domains exclude_domains: Filter results to exclude these domains
        include_terms: Filter results to only include these terms exclude_terms: Filter
        results to exclude these terms

        Returns: JSON response with formatted search results

        Args:
          query: Search query string

          country: Country code (e.g., 'us', 'gb')

          crawl_end_date: End date for crawled content (YYYY-MM-DD)

          crawl_start_date: Start date for crawled content (YYYY-MM-DD)

          exclude_domains: Domains to exclude from search results

          exclude_terms: Terms that must be excluded from search results

          include_domains: Domains to include in search results

          include_terms: Terms that must be included in search results

          language: ISO language code (e.g., 'en', 'fr')

          max_results: Maximum number of results to return

          provider: Search provider to use

          published_end_date: End date for published content (YYYY-MM-DD)

          published_start_date: Start date for published content (YYYY-MM-DD)

          summarize: Whether to generate a summary of results using LLM

          topic: Search topic category

          use_selenium: Whether to enhance DuckDuckGo results with Selenium (only applies to DuckDuckGo
              provider)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "country": country,
                        "crawl_end_date": crawl_end_date,
                        "crawl_start_date": crawl_start_date,
                        "exclude_domains": exclude_domains,
                        "exclude_terms": exclude_terms,
                        "include_domains": include_domains,
                        "include_terms": include_terms,
                        "language": language,
                        "max_results": max_results,
                        "provider": provider,
                        "published_end_date": published_end_date,
                        "published_start_date": published_start_date,
                        "summarize": summarize,
                        "topic": topic,
                        "use_selenium": use_selenium,
                    },
                    v1_search_params.V1SearchParams,
                ),
            ),
            cast_to=V1SearchResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def extract(self) -> AsyncExtractResource:
        return AsyncExtractResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/agent-toolkit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/agent-toolkit-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def get_credits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetCreditsResponse:
        """
        Get current credit usage and limits for the authenticated user.

        Returns: CreditResponse with total, used, and remaining credits
        """
        return await self._get(
            "/api/v1/credits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetCreditsResponse,
        )

    async def search(
        self,
        *,
        query: str,
        country: Optional[str] | NotGiven = NOT_GIVEN,
        crawl_end_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        crawl_start_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        exclude_domains: Optional[List[str]] | NotGiven = NOT_GIVEN,
        exclude_terms: Optional[List[str]] | NotGiven = NOT_GIVEN,
        include_domains: Optional[List[str]] | NotGiven = NOT_GIVEN,
        include_terms: Optional[List[str]] | NotGiven = NOT_GIVEN,
        language: Optional[str] | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        provider: Optional[Literal["google", "bing", "duckduckgo"]] | NotGiven = NOT_GIVEN,
        published_end_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        published_start_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        summarize: bool | NotGiven = NOT_GIVEN,
        topic: Literal["general", "news", "images", "videos", "finance"] | NotGiven = NOT_GIVEN,
        use_selenium: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1SearchResponse:
        """
        Search endpoint that returns formatted results from external search provider.

        Args: query: The search query string language: Optional ISO language code (e.g.,
        'en', 'fr') country: Optional country code (e.g., 'us', 'gb') max_results:
        Maximum number of results to return (1-10) summarize: Whether to generate a
        summary of results using LLM provider: Search provider to use (google, bing,
        duckduckgo) topic: Search topic category use_selenium: Whether to enhance
        DuckDuckGo results with Selenium published_start_date: Filter results published
        after this date published_end_date: Filter results published before this date
        crawl_start_date: Filter results crawled after this date crawl_end_date: Filter
        results crawled before this date include_domains: Filter results to only include
        these domains exclude_domains: Filter results to exclude these domains
        include_terms: Filter results to only include these terms exclude_terms: Filter
        results to exclude these terms

        Returns: JSON response with formatted search results

        Args:
          query: Search query string

          country: Country code (e.g., 'us', 'gb')

          crawl_end_date: End date for crawled content (YYYY-MM-DD)

          crawl_start_date: Start date for crawled content (YYYY-MM-DD)

          exclude_domains: Domains to exclude from search results

          exclude_terms: Terms that must be excluded from search results

          include_domains: Domains to include in search results

          include_terms: Terms that must be included in search results

          language: ISO language code (e.g., 'en', 'fr')

          max_results: Maximum number of results to return

          provider: Search provider to use

          published_end_date: End date for published content (YYYY-MM-DD)

          published_start_date: Start date for published content (YYYY-MM-DD)

          summarize: Whether to generate a summary of results using LLM

          topic: Search topic category

          use_selenium: Whether to enhance DuckDuckGo results with Selenium (only applies to DuckDuckGo
              provider)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "country": country,
                        "crawl_end_date": crawl_end_date,
                        "crawl_start_date": crawl_start_date,
                        "exclude_domains": exclude_domains,
                        "exclude_terms": exclude_terms,
                        "include_domains": include_domains,
                        "include_terms": include_terms,
                        "language": language,
                        "max_results": max_results,
                        "provider": provider,
                        "published_end_date": published_end_date,
                        "published_start_date": published_start_date,
                        "summarize": summarize,
                        "topic": topic,
                        "use_selenium": use_selenium,
                    },
                    v1_search_params.V1SearchParams,
                ),
            ),
            cast_to=V1SearchResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.get_credits = to_raw_response_wrapper(
            v1.get_credits,
        )
        self.search = to_raw_response_wrapper(
            v1.search,
        )

    @cached_property
    def extract(self) -> ExtractResourceWithRawResponse:
        return ExtractResourceWithRawResponse(self._v1.extract)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.get_credits = async_to_raw_response_wrapper(
            v1.get_credits,
        )
        self.search = async_to_raw_response_wrapper(
            v1.search,
        )

    @cached_property
    def extract(self) -> AsyncExtractResourceWithRawResponse:
        return AsyncExtractResourceWithRawResponse(self._v1.extract)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.get_credits = to_streamed_response_wrapper(
            v1.get_credits,
        )
        self.search = to_streamed_response_wrapper(
            v1.search,
        )

    @cached_property
    def extract(self) -> ExtractResourceWithStreamingResponse:
        return ExtractResourceWithStreamingResponse(self._v1.extract)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.get_credits = async_to_streamed_response_wrapper(
            v1.get_credits,
        )
        self.search = async_to_streamed_response_wrapper(
            v1.search,
        )

    @cached_property
    def extract(self) -> AsyncExtractResourceWithStreamingResponse:
        return AsyncExtractResourceWithStreamingResponse(self._v1.extract)
