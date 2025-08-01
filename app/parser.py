import re

from bs4 import BeautifulSoup
from requests.models import Response

from app.models import User


class Parser:
    @staticmethod
    def extract_token_and_session(html: Response) -> tuple[str, str]:
        cookies = html.cookies.get_dict()
        data = html.text
        match = re.search(r'name="token" value="([^"]+)"', data)
        token = match.group(1) if match else None
        set_session = cookies.get("phpMyAdmin")
        return token, set_session

    @staticmethod
    def extract_link_by_text(html: Response, link_text: str) -> str:
        link = (
            BeautifulSoup(html.text, "html.parser")
            .find("a", string=lambda s: s.strip() == link_text)
            .get("href")
        )

        return link

    @staticmethod
    def extract_users_from_html(html: Response) -> list[User]:
        users = []

        rows = BeautifulSoup(html.text, "html.parser").find("tbody").find_all("tr")

        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 6:
                id_cell = cells[4].get_text(strip=True)
                name_cell = cells[5].get_text(strip=True)
                users.append(
                    User(
                        id=int(id_cell),
                        name=name_cell,
                    )
                )

        return users
