# file: gateway_orchestrator/app/services/router_service.py
from .intent_service import resolve_agent
from ..clients import hr_agent_client, data_agent_client
# you would also import workflow_agent_client, support_agent_client


async def route_request(req: dict) -> dict:
    """
    req is a dict from UserRequest model: {channel, user_id, intent, payload}
    """
    intent = req.get("intent", "")
    payload = req.get("payload", {}) or {}

    agent = resolve_agent(intent)

    if agent == "HR":
        if intent == "apply_leave":
            return await hr_agent_client.apply_leave(payload)
        if intent == "onboard_employee":
            return await hr_agent_client.onboard_employee(payload)

    if agent == "DATA":
        return await data_agent_client.generate_report(payload)

    # TODO: Add WORKFLOW & SUPPORT routing

    return {"error": f"Unknown or unsupported intent: {intent}"}
