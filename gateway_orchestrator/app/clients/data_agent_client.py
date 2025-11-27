# file: gateway_orchestrator/app/clients/data_agent_client.py
import httpx
from common.config import settings
from common.logging_utils import setup_logging

logger = setup_logging("data_agent_client")


async def generate_report(payload: dict) -> dict:
    url = f"{settings.DATA_AGENT_URL}/analytics/report"
    logger.info(f"Calling Data Agent: {url} payload={payload}")
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=payload, timeout=20)
        resp.raise_for_status()
        return resp.json()
