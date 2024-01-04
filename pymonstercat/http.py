import os
from pathlib import Path
import sys
import time

from dotenv import dotenv_values, set_key
from httpx import Client, Cookies, Response, ConnectError, __version__ as httpx_version

from . import __version__


class HTTPClient:
    __domain = "player.monstercat.app"
    __user_agent = (
        f"PyMonstercat v.{__version__} (https://github.com/L4zzur/pymonstercat), "
        f"Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}, "
        f"httpx {httpx_version}"
    )

    def __init__(self, config_path: Path) -> None:
        self.__client = Client()
        self.__config_path = config_path
        self.__config = dotenv_values(self.__config_path)
        print(self.__config)
        self.__client.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.__user_agent,
        }

        if "COOKIE" in self.__config:
            cookie = self.__config["COOKIE"]
            self.set_cookies(cookie)

    @staticmethod
    def catch_connect_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ConnectError as error:
                print("Connection error")
                exit()

        return wrapper

    @catch_connect_error
    def post(self, url: str, json: dict | None = None) -> Response:
        return self.__client.post(url=url, json=json)

    @catch_connect_error
    def get(self, url: str, params: dict | None = None) -> Response:
        return self.__client.get(url=url, params=params)

    def set_cookies(self, cookie: str) -> None:
        self.__client.cookies = Cookies()
        self.__client.cookies.set(name="cid", value=cookie, domain=self.__domain)

    def get_cookies(self) -> str:
        return self.__client.cookies.get("cid")

    def has_cookies(self) -> bool:
        return "COOKIE" in self.__config

    def import_cookies(self) -> None:
        cookie = self.__config["COOKIE"]
        self.set_cookies(cookie)

    def export_cookies(self) -> None:
        set_key(
            dotenv_path=self.__config_path,
            key_to_set="COOKIE",
            value_to_set=self.get_cookies(),
        )
        set_key(
            dotenv_path=self.__config_path,
            key_to_set="COOKIE_EXPIRY",
            value_to_set=str(int(time.time()) + 30 * 24 * 60 * 60),
        )
