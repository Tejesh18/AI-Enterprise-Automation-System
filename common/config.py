# file: common/config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Enterprise Automation"
    ENV: str = "local"
    DEBUG: bool = True

    # Gateway
    GATEWAY_HOST: str = "0.0.0.0"
    GATEWAY_PORT: int = 8000

    # Agent URLs (internal service URLs)
    HR_AGENT_URL: str = "http://localhost:8101"
    DATA_AGENT_URL: str = "http://localhost:8102"
    WORKFLOW_AGENT_URL: str = "http://localhost:8103"
    SUPPORT_AGENT_URL: str = "http://localhost:8104"

    # Message broker (placeholder)
    BROKER_URL: str = "kafka://localhost:9092"

    class Config:
        env_file = ".env"


settings = Settings()
