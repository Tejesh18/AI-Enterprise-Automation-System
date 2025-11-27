# file: common/messaging.py
from typing import Callable, Any
from .logging_utils import setup_logging
from .config import settings

logger = setup_logging("messaging")


class MessageBus:
    """
    Simple abstraction for a message bus.
    In a real system, this would wrap Kafka/RabbitMQ/etc.
    """

    def __init__(self, broker_url: str):
        self.broker_url = broker_url
        logger.info(f"MessageBus initialized with broker: {broker_url}")

    async def publish(self, topic: str, payload: dict) -> None:
        # TODO: integrate with real broker
        logger.info(f"[PUBLISH] topic={topic}, payload={payload}")

    async def subscribe(self, topic: str, handler: Callable[[dict], Any]) -> None:
        # TODO: integrate with real broker consumer
        logger.info(f"[SUBSCRIBE] topic={topic}, handler={handler.__name__}")
        # placeholder: in real code, this would run a consumer loop


message_bus = MessageBus(settings.BROKER_URL)
