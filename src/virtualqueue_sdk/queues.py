from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import requests

from virtualqueue_sdk.config import API_BASE_PATH

QUEUES_API_URL = f"{API_BASE_PATH}queue/"


@dataclass
class VerificationResultData:
    token: str
    started_at: datetime
    finished_at: datetime


@dataclass
class VerificationResult:
    message: str
    success: bool
    data: Optional[VerificationResultData] = None


def verify_finished_line(token: str) -> VerificationResult:
    response = requests.get(f"{QUEUES_API_URL}verify?token={token}")
    if response.status_code == 400:
        return VerificationResult(success=False, message="Please double-check input token.")

    response_data = response.json()

    if response.status_code == 404:
        return VerificationResult(success=False, message=response_data["message"])

    return VerificationResult(success=True,
                              message=response_data["message"],
                              data=VerificationResultData(token=response_data["data"]["token"],
                                                          started_at=response_data["data"]["finished_line"]["ingressed_at"],
                                                          finished_at=response_data["data"]["finished_line"]["finished_at"]))
