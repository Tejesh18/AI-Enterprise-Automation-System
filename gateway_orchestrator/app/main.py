# file: gateway_orchestrator/app/main.py
from fastapi import FastAPI
from common.config import settings
from common.logging_utils import setup_logging
from .routes import health, orchestration

logger = setup_logging("gateway")


app = FastAPI(
    title="Enterprise Automation Gateway",
    description="API Gateway and Orchestration Layer",
    version="1.0.0",
)


@app.on_event("startup")
async def on_startup():
    logger.info("Gateway starting up...")


@app.on_event("shutdown")
async def on_shutdown():
    logger.info("Gateway shutting down...")


app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(orchestration.router, prefix="/api/v1", tags=["orchestration"])
