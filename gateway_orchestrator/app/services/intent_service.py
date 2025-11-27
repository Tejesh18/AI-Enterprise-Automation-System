# file: gateway_orchestrator/app/services/intent_service.py
from typing import Literal

AgentType = Literal["HR", "DATA", "WORKFLOW", "SUPPORT", "UNKNOWN"]


def resolve_agent(intent: str) -> AgentType:
    """
    Simple intent → agent mapping.
    Can be replaced with NLP/LLM later.
    """
    intent = intent.lower()

    if intent in {"apply_leave", "onboard_employee", "get_salary_info"}:
        return "HR"
    if intent in {"get_report", "sales_analytics", "kpi_summary"}:
        return "DATA"
    if intent in {"start_approval", "route_task", "escalate_issue"}:
        return "WORKFLOW"
    if intent in {"raise_ticket", "customer_query", "check_status"}:
        return "SUPPORT"

    return "UNKNOWN"
