# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["V1GetCreditsResponse"]


class V1GetCreditsResponse(BaseModel):
    days_until_reset: int

    free_credits: int

    period: str

    remaining_credits: int

    reset_date: str

    total_credits: int

    used_credits: int

    plan_tier: Optional[str] = None

    purchased_credits: Optional[int] = None
