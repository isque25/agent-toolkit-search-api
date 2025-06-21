# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from agent_toolkit import AgentToolkit, AsyncAgentToolkit
from agent_toolkit.types.api.v1 import ExtractResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: AgentToolkit) -> None:
        extract = client.api.v1.extract.create(
            urls=["string"],
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: AgentToolkit) -> None:
        extract = client.api.v1.extract.create(
            urls=["string"],
            extract_depth="basic",
            include_images=True,
            include_links=True,
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: AgentToolkit) -> None:
        response = client.api.v1.extract.with_raw_response.create(
            urls=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: AgentToolkit) -> None:
        with client.api.v1.extract.with_streaming_response.create(
            urls=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AgentToolkit) -> None:
        extract = client.api.v1.extract.retrieve(
            url="url",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: AgentToolkit) -> None:
        extract = client.api.v1.extract.retrieve(
            url="url",
            extract_depth="extract_depth",
            include_images=True,
            include_links=True,
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AgentToolkit) -> None:
        response = client.api.v1.extract.with_raw_response.retrieve(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AgentToolkit) -> None:
        with client.api.v1.extract.with_streaming_response.retrieve(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncAgentToolkit) -> None:
        extract = await async_client.api.v1.extract.create(
            urls=["string"],
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAgentToolkit) -> None:
        extract = await async_client.api.v1.extract.create(
            urls=["string"],
            extract_depth="basic",
            include_images=True,
            include_links=True,
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAgentToolkit) -> None:
        response = await async_client.api.v1.extract.with_raw_response.create(
            urls=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAgentToolkit) -> None:
        async with async_client.api.v1.extract.with_streaming_response.create(
            urls=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAgentToolkit) -> None:
        extract = await async_client.api.v1.extract.retrieve(
            url="url",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAgentToolkit) -> None:
        extract = await async_client.api.v1.extract.retrieve(
            url="url",
            extract_depth="extract_depth",
            include_images=True,
            include_links=True,
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAgentToolkit) -> None:
        response = await async_client.api.v1.extract.with_raw_response.retrieve(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAgentToolkit) -> None:
        async with async_client.api.v1.extract.with_streaming_response.retrieve(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True
