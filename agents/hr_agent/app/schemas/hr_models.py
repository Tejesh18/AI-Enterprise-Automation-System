# file: agents/hr_agent/app/schemas/hr_models.py
from pydantic import BaseModel, EmailStr
from typing import Optional


class OnboardingRequest(BaseModel):
    employee_id: str
    name: str
    email: EmailStr
    department: str
    designation: Optional[str] = None


class OnboardingResponse(BaseModel):
    employee_id: str
    status: str
    message: str


class LeaveRequest(BaseModel):
    employee_id: str
    days: int
    reason: str


class LeaveResponse(BaseModel):
    employee_id: str
    approved: bool
    remaining_leaves: int
    message: str
