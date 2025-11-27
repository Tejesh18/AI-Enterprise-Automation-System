# file: gateway_orchestrator/app/schemas/response_schemas.py
from pydantic import BaseModel
from typing import Any


class OrchestrationResponse(BaseModel):
    status: str
    data: Any
    message: str = "OK"
