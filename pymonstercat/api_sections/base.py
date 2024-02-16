import sys
import time
from pathlib import Path

import yaml
from httpx import Client, ConnectError, Cookies, Response
from httpx import __version__ as httpx_version

from .. import __version__


class ConfigObject:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                value = ConfigObject(value)
            self.__dict__[key] = value

    def __getattr__(self, item):
        return self.__dict__.get(item, None)

    def __getitem__(self, item):
        return self.__dict__.get(item, None)

    def to_dict(self):
        return {
            key: value.to_dict() if isinstance(value, ConfigObject) else value
            for key, value in self.__dict__.items()
        }


class PyMonstercatBase:
    BASE = "https://player.monstercat.app/api/"
    CDX = "https://cdx.monstercat.com"

    __domain = "player.monstercat.app"
    __user_agent = (
        f"PyMonstercat v.{__version__}"
        f"(https://github.com/L4zzur/pymonstercat), "
        f"Python"
        f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}, "
        f"httpx {httpx_version}"
    )

    def __init__(self, config_path: Path) -> None:
        self.__client = Client()
        self.__client.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.__user_agent,
        }

        self.__config_path = config_path
        if not self.__config_path.exists():
            self.create_config()
        self.load_config()

    def get_config_path(self) -> Path:
        return self.__config_path

    def create_config(self) -> None:
        self.__config = ConfigObject(
            {
                "creds": {"email": None, "password": None},
                "cookie": {"value": None, "expires": None},
                "remember_me": True,
            }
        )
        self.save_config()

    def load_config(self) -> None:
        with open(self.__config_path, "r") as f:
            self.__config = ConfigObject(yaml.safe_load(f))

    def save_config(self) -> None:
        with open(self.__config_path, "w") as f:
            yaml.dump(self.__config.to_dict(), f)

    @staticmethod
    def catch_connect_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ConnectError:
                print("Connection error.")
                exit()

        return wrapper

    @catch_connect_error
    def post(
        self,
        url: str,
        json: dict | None = None,
    ) -> Response:
        return self.__client.post(
            url=url,
            json=json,
        )

    @catch_connect_error
    def get(
        self,
        url: str,
        params: dict | None = None,
        follow_redirects: bool = False,
    ) -> Response:
        return self.__client.get(
            url=url,
            params=params,
            follow_redirects=follow_redirects,
        )

    def has_creds(self) -> bool:
        return bool(self.get_email()) and bool(self.get_password())

    def set_email(self, email: str) -> None:
        self.__config.creds.email = email
        self.save_config()

    def set_password(self, password: str) -> None:
        self.__config.creds.password = password
        self.save_config()

    def get_email(self) -> str:
        return self.__config.creds.email

    def get_password(self) -> str:
        return self.__config.creds.password

    def remove_creds(self) -> None:
        self.__config.creds.email = None
        self.__config.creds.password = None
        self.save_config()

    def has_cookies(self) -> bool:
        return bool(self.__config.cookie.value)

    def __get_cookies(self) -> str | None:
        return self.__client.cookies.get("cid")

    def set_cookies(self, cookie: str) -> None:
        self.__client.cookies = Cookies()
        self.__client.cookies.set(
            name="cid",
            value=cookie,
            domain=self.__domain,
        )

    def import_cookies(self) -> None:
        cookie = self.__config.cookie.value
        self.set_cookies(cookie)

    def export_cookies(self) -> None:
        self.__config.cookie.value = self.__get_cookies()
        self.__config.cookie.expires = int(time.time()) + 30 * 86400
        self.save_config()

    def remove_cookies(self) -> None:
        self.__config.cookie.value = None
        self.__config.cookie.expires = None
        self.save_config()
