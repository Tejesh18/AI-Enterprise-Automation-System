# file: agents/hr_agent/app/main.py
from fastapi import FastAPI
from common.logging_utils import setup_logging
from .routes import health, hr_ops

logger = setup_logging("hr_agent")

app = FastAPI(
    title="HR Automation Agent",
    description="Handles HR workflows like onboarding and leave",
    version="1.0.0",
)


@app.on_event("startup")
async def on_startup():
    logger.info("HR Agent starting up...")


@app.on_event("shutdown")
async def on_shutdown():
    logger.info("HR Agent shutting down...")


app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(hr_ops.router, prefix="/hr", tags=["hr"])
