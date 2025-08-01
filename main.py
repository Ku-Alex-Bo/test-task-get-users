import logging.config
import os

from app.worker import run_worker

if __name__ == "__main__":
    logging.config.fileConfig(
        fname=os.path.join(os.path.dirname(__file__), "config", "logging.conf"),
        disable_existing_loggers=False,
    )

    run_worker()
