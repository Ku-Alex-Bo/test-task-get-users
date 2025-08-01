import logging
import time

from tabulate import tabulate

from app.client import HTTPClient
from app.parser import Parser
from config.config import settings

logger = logging.getLogger(__name__)


def run_worker():
    logger.info("===! START !===")

    client = HTTPClient()

    # 1. Get the initial page to extract token and session

    logger.info("1. Get token and session")
    html = client.get()
    token, set_session = Parser.extract_token_and_session(html)
    time.sleep(0.7)

    # 2. Login and get testDB link

    logger.info("2. Get testDB link")
    html = client.post(
        data={
            "pma_username": settings.LOGIN,
            "pma_password": settings.PASS,
            "token": token,
            "set_session": set_session,
        }
    )
    testDB_link = Parser.extract_link_by_text(html, "testDB")
    time.sleep(0.7)

    # 3. Get the users table link

    logger.info("3. Get users table link")
    html = client.get(
        path=testDB_link,
        params={
            "token": token,
        },
    )
    users_table_link = Parser.extract_link_by_text(html, "users")
    time.sleep(0.7)

    # 4. Get users from the users table

    logger.info("4. Extract users ")
    html = client.get(
        path=users_table_link,
        params={
            "token": token,
        },
    )
    users = Parser.extract_users_from_html(html)
    time.sleep(0.7)

    # 5. Print users in a table format

    logger.info("5. Print users")
    table = tabulate([[user.id, user.name] for user in users], headers=["ID", "Name"])
    print(table)

    logger.info("===! END !===")
