from dataclasses import dataclass

from dataclass_wizard import JSONSerializable


@dataclass
class Link(JSONSerializable):
    """Class represents Link object

    Attributes:
        platform (`str`): The platform this link leads to.
        url (`str`): The url this link leads to.
    """

    platform: str
    url: str

    class Meta(JSONSerializable.Meta):
        json_key_to_field = {
            "Platform": "platform",
            "Url": "url",
        }

    def __str__(self):
        return f"Link:\nplatform = {self.platform}\nurl = {self.url}"
