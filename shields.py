#!/usr/bin/env python3
"""shields.io badge url generator."""

from enum import Enum

SHIELDS_URL = "https://img.shields.io/badge/"


def snake_case_to_camel_case(token: str) -> str:
    """Convert a snake_case token to a camelCase token.

    Args:
        token (str): The snake_case token to convert to camelCase.

    Returns:
        str: The camelCase token.

    """
    while (i := token.find("_")) != -1:
        token = token[:i] + token[i + 1].upper() + token[i + 2 :]
    return token


class BadgeStyle(Enum):
    """The five different Badge rendering styles."""

    FLAT = "flat"
    FLAT_SQUARE = "flat-square"
    PLASTIC = "plastic"
    FTB = "for-the-badge"
    SOCIAL = "social"

    def __repr__(self) -> str:
        return super().__str__()

    def __str__(self) -> str:
        return self.value


class BadgeContent:
    """The primary content of the Badge."""

    __slots__ = ("color", "label", "message")

    label: str
    message: str | None
    color: str

    @staticmethod
    def _santize_field(field: str) -> str:
        return field.replace(" ", "%20").replace("_", "__").replace("-", "--")

    def __init__(self, label: str, color: str, message: str | None = None):
        self.label = self._santize_field(label)
        self.message = self._santize_field(message) if message is not None else None
        self.color = self._santize_field(color)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.label}, {self.color}, {self.message})"

    def __str__(self) -> str:
        return (
            f"{self.label}-{self.message}-{self.color}"
            if self.message is not None
            else f"{self.label}-{self.color}"
        )


class BadgeConfig:
    """The auxiliary configuration for the Badge."""

    __slots__ = ("cache_seconds", "logo", "logo_color", "style")

    style: BadgeStyle | None
    logo: str | None
    logo_color: str | None
    cache_seconds: int | None

    def __init__(
        self,
        *,
        style: BadgeStyle | None = None,
        logo: str | None = None,
        logo_color: str | None = None,
        cache_seconds: int | None = None,
    ):
        self.style = style
        self.logo = logo
        self.logo_color = logo_color
        self.cache_seconds = cache_seconds

    def __repr__(self) -> str:
        kwargs = []
        for key in self.__slots__:
            if val := self.__getattribute__(key):
                kwargs.append(f"{key}={repr(val)}")

        return f"{self.__class__.__name__}({', '.join(kwargs)})"

    def __str__(self) -> str:
        ret = ""
        for key in self.__slots__:
            if val := self.__getattribute__(key):
                ret += (
                    f"{'?' if ret == '' else '&'}{snake_case_to_camel_case(key)}={val}"
                )
        return ret


class Badge:
    """Shields.io Badge."""

    __slots__ = ("config", "content", "host")

    content: BadgeContent
    config: BadgeConfig
    host: str

    def __init__(
        self,
        label: str,
        color: str,
        message: str | None = None,
        *,
        style: BadgeStyle | None = None,
        logo: str | None = None,
        logo_color: str | None = None,
        cache_seconds: int | None = None,
        host: str | None = None,
    ):
        self.content = BadgeContent(label, color, message)
        self.config = BadgeConfig(
            style=style,
            logo=logo,
            logo_color=logo_color,
            cache_seconds=cache_seconds,
        )
        self.host = host or SHIELDS_URL

    def __repr__(self) -> str:
        pargs = ", ".join(
            [
                *[
                    repr(self.content.__getattribute__(key))
                    for key in ("label", "color")
                ],
                *([repr(self.content.message)] if self.content.message else []),
            ]
        )

        kwargs = ", ".join(
            [
                f"{key}={repr(val)}"
                for key, val in filter(
                    lambda pair: pair[1] is not None,
                    [
                        (key, self.config.__getattribute__(key))
                        for key in BadgeConfig.__slots__
                    ],
                )
            ]
        )

        return (
            f"{self.__class__.__name__}({pargs}{', ' + kwargs if kwargs != '' else ''})"
        )

    def __str__(self) -> str:
        return f"{self.host}{self.content}{self.config}"
