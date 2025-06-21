# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from agent_toolkit import AgentToolkit, AsyncAgentToolkit
from agent_toolkit._utils import parse_date
from agent_toolkit.types.api import V1SearchResponse, V1GetCreditsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_credits(self, client: AgentToolkit) -> None:
        v1 = client.api.v1.get_credits()
        assert_matches_type(V1GetCreditsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_credits(self, client: AgentToolkit) -> None:
        response = client.api.v1.with_raw_response.get_credits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetCreditsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_credits(self, client: AgentToolkit) -> None:
        with client.api.v1.with_streaming_response.get_credits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetCreditsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_search(self, client: AgentToolkit) -> None:
        v1 = client.api.v1.search(
            query="query",
        )
        assert_matches_type(V1SearchResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_search_with_all_params(self, client: AgentToolkit) -> None:
        v1 = client.api.v1.search(
            query="query",
            country="country",
            crawl_end_date=parse_date("2019-12-27"),
            crawl_start_date=parse_date("2019-12-27"),
            exclude_domains=["string"],
            exclude_terms=["string"],
            include_domains=["string"],
            include_terms=["string"],
            language="language",
            max_results=1,
            provider="google",
            published_end_date=parse_date("2019-12-27"),
            published_start_date=parse_date("2019-12-27"),
            summarize=True,
            topic="general",
            use_selenium=True,
        )
        assert_matches_type(V1SearchResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_search(self, client: AgentToolkit) -> None:
        response = client.api.v1.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1SearchResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_search(self, client: AgentToolkit) -> None:
        with client.api.v1.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1SearchResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_credits(self, async_client: AsyncAgentToolkit) -> None:
        v1 = await async_client.api.v1.get_credits()
        assert_matches_type(V1GetCreditsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_credits(self, async_client: AsyncAgentToolkit) -> None:
        response = await async_client.api.v1.with_raw_response.get_credits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetCreditsResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_credits(self, async_client: AsyncAgentToolkit) -> None:
        async with async_client.api.v1.with_streaming_response.get_credits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetCreditsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_search(self, async_client: AsyncAgentToolkit) -> None:
        v1 = await async_client.api.v1.search(
            query="query",
        )
        assert_matches_type(V1SearchResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncAgentToolkit) -> None:
        v1 = await async_client.api.v1.search(
            query="query",
            country="country",
            crawl_end_date=parse_date("2019-12-27"),
            crawl_start_date=parse_date("2019-12-27"),
            exclude_domains=["string"],
            exclude_terms=["string"],
            include_domains=["string"],
            include_terms=["string"],
            language="language",
            max_results=1,
            provider="google",
            published_end_date=parse_date("2019-12-27"),
            published_start_date=parse_date("2019-12-27"),
            summarize=True,
            topic="general",
            use_selenium=True,
        )
        assert_matches_type(V1SearchResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncAgentToolkit) -> None:
        response = await async_client.api.v1.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1SearchResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncAgentToolkit) -> None:
        async with async_client.api.v1.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1SearchResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
