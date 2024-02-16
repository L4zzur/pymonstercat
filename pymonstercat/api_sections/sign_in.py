from icecream import ic

from pymonstercat.api_exceptions import ConfigHasNoCreds
from pymonstercat.api_sections.base import PyMonstercatBase


class PyMonstercatAuth(PyMonstercatBase):
    SIGN_IN = PyMonstercatBase.BASE + "sign-in"

    def sign_in_email(
        self,
        email: str | None = None,
        password: str | None = None,
    ) -> bool:
        if email is not None and password is not None:
            ic("Setting email and password in yaml config.")
            self.set_email(email)
            self.set_password(password)
        elif email is None or password is None:
            ic("Loading email and password from yaml config.")
            if self.has_cookies():
                ic("Using cookie from yaml config.")
                self.import_cookies()
                return True
            elif not self.has_creds():
                raise ConfigHasNoCreds(
                    "No credentials found in " + f"{self.get_config_path().name}."
                )

        payload = {
            "Email": self.get_email(),
            "Password": self.get_password(),
        }
        url = self.SIGN_IN
        response = self.post(
            url=url,
            json=payload,
        )

        if response.status_code == 200:
            ic("Sign in successful")
            self.save_config()
            self.export_cookies()
            return True

        ic("Sign in failed")
        self.remove_creds()
        self.remove_cookies()
        return False
