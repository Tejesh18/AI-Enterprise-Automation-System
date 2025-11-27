# file: agents/hr_agent/app/routes/hr_ops.py
from fastapi import APIRouter
from ..schemas.hr_models import (
    OnboardingRequest,
    OnboardingResponse,
    LeaveRequest,
    LeaveResponse,
)
from ..services.onboarding_service import process_onboarding
from ..services.leave_service import apply_leave

router = APIRouter()


@router.post("/onboarding", response_model=OnboardingResponse)
async def onboarding(req: OnboardingRequest):
    return await process_onboarding(req)


@router.post("/leave", response_model=LeaveResponse)
async def leave(req: LeaveRequest):
    return await apply_leave(req)
