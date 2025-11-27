# file: agents/hr_agent/app/services/onboarding_service.py
from ..schemas.hr_models import OnboardingRequest, OnboardingResponse
from ..integrators.hrms_adapter import create_employee_in_hrms


async def process_onboarding(req: OnboardingRequest) -> OnboardingResponse:
    # Call the HRMS / DB layer
    success = await create_employee_in_hrms(req)

    if success:
        return OnboardingResponse(
            employee_id=req.employee_id,
            status="created",
            message="Employee onboarding initiated successfully.",
        )
    else:
        return OnboardingResponse(
            employee_id=req.employee_id,
            status="failed",
            message="Failed to onboard employee. Please retry.",
        )
