import logging

import requests

from config.config import settings

logger = logging.getLogger(__name__)


class HTTPClient:
    base_url = settings.BASE_URL

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/114.0.0.0 Safari/537.36"
                ),
            }
        )

    def request(self, method: str, path: str = "", **kwargs) -> requests.Response:

        url = f"{self.base_url}/{path}"
        logger.info("HTTP %s %s", method, url)
        try:
            resp = self.session.request(
                method=method.upper(), url=url, timeout=5, **kwargs
            )
        except requests.RequestException as e:
            logger.error("Request failed: %s", e)
            return

        if not resp.ok:
            logger.error("Unexpected HTTP status: %s", resp.status_code)

        return resp

    def get(self, path: str = "", **kwargs) -> requests.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str = "", **kwargs) -> requests.Response:
        return self.request("POST", path, **kwargs)
