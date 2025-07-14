from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional
from uuid import UUID

import requests

from ._config import API_BASE_PATH

QUEUES_API_URL = Path(API_BASE_PATH).joinpath("queue/")
VERIFY_API_URL = QUEUES_API_URL.joinpath("verify")


@dataclass
class VerificationResultData:
    token: str
    ingressed_at: datetime
    finished_at: datetime


@dataclass
class VerificationResult:
    message: str
    success: bool
    data: Optional[VerificationResultData] = None


def verify_token(token: str) -> VerificationResult:
    try:
        uuid_token = UUID(token, version=4)
    except ValueError:
        return VerificationResult(success=False, message="Invalid UUID")

    response = requests.get(f"{VERIFY_API_URL}?token={uuid_token}")

    response_data = response.json()

    if 200 <= response.status_code < 300:
        return VerificationResult(
            success=True,
            message=response_data["message"],
            data=VerificationResultData(
                token=response_data["data"]["token"],
                ingressed_at=response_data["data"]["finished_line"]["ingressed_at"],
                finished_at=response_data["data"]["finished_line"]["finished_at"],
            ),
        )

    if 400 <= response.status_code < 500:
        return VerificationResult(success=False, message=response_data["message"])

    return VerificationResult(success=False, message="Please double check your token")
