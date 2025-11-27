# file: gateway_orchestrator/app/schemas/request_schemas.py
from pydantic import BaseModel
from typing import Dict, Any


class UserRequest(BaseModel):
    channel: str              # "web", "chat", etc.
    user_id: str
    intent: str               # "apply_leave", "get_report", etc.
    payload: Dict[str, Any]
