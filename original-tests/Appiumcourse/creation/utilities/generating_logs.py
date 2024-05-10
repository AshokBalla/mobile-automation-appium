import logging

logging.basicConfig(filename="../logs/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

# Create logger instance
logger = logging.getLogger(__name__)

logger.info("This is an info message")