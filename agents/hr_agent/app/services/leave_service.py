# file: agents/hr_agent/app/services/leave_service.py
from ..schemas.hr_models import LeaveRequest, LeaveResponse


async def apply_leave(req: LeaveRequest) -> LeaveResponse:
    # In a real system, you would:
    # 1. Fetch employee leave balance from DB / HRMS
    # 2. Validate
    # 3. Update balance and create leave record
    # For now, simple mock logic:
    total_leaves = 20
    used_leaves = 5
    requested = req.days

    remaining = total_leaves - used_leaves - requested
    approved = remaining >= 0

    if not approved:
        remaining = total_leaves - used_leaves  # original remaining

    message = "Leave approved." if approved else "Insufficient leave balance."

    return LeaveResponse(
        employee_id=req.employee_id,
        approved=approved,
        remaining_leaves=remaining,
        message=message,
    )
