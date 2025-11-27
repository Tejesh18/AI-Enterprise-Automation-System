# file: gateway_orchestrator/app/routes/orchestration.py
from fastapi import APIRouter, Depends, HTTPException
from ..schemas.request_schemas import UserRequest
from ..schemas.response_schemas import OrchestrationResponse
from ..services.router_service import route_request
from common.security import get_api_key

router = APIRouter()


@router.post("/handle", response_model=OrchestrationResponse)
async def handle_request(
    req: UserRequest,
    api_key: str = Depends(get_api_key)
):
    try:
        data = await route_request(req.dict())
        return OrchestrationResponse(status="success", data=data, message="OK")
    except Exception as exc:
        # In production, log and sanitize exception
        raise HTTPException(status_code=500, detail=str(exc))
