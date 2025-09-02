import logging
import sys

import structlog

def configure_logging():

    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.DEBUG,
    )

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso", utc=False), # Timestamp in local time
            structlog.stdlib.add_log_level,
            structlog.stdlib.add_logger_name,
            structlog.processors.JSONRenderer()
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
    )


def log_5w1h(who: str, what: str, where: str, why: str, how: str, log_level: str = "info"):
    """
    Log a message using the 5W1H method (Who, What, Where, Why, How).
    """

    log = structlog.get_logger("app.logging_config")

    log_method = getattr(log, log_level.lower(), log.info)

    message = {
        "who": who,
        "what": what,
        "where": where,
        "why": why,
        "how": how
    }

    log_method(
        "log-entry",
        data=message
    )

configure_logging()