# file: gateway_orchestrator/app/clients/hr_agent_client.py
import httpx
from common.config import settings
from common.logging_utils import setup_logging

logger = setup_logging("hr_agent_client")


async def apply_leave(payload: dict) -> dict:
    """
    Calls HR agent's /hr/leave endpoint.
    """
    url = f"{settings.HR_AGENT_URL}/hr/leave"
    logger.info(f"Calling HR Agent: {url} payload={payload}")
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json()


async def onboard_employee(payload: dict) -> dict:
    url = f"{settings.HR_AGENT_URL}/hr/onboarding"
    logger.info(f"Calling HR Agent: {url} payload={payload}")
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json()
