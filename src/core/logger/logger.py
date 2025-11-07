from loguru import logger
import sys, os

# создаём папку logs если её нет
os.makedirs("logs", exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    format="{time} {level} {message}"
)

logger.add(
    "logs/app.log",
    level="DEBUG",
    rotation="10 MB",
    retention="7 days",
    compression="zip"
)
