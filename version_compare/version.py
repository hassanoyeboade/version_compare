from typing import NoReturn

from .parsers import parse_version
from .validators import validate_version


class Version(tuple):
    def __init__(self, version_string: str) -> NoReturn:
        version_string = validate_version(version_string)
        self.raw_value = version_string

    def __new__(cls, version_string: str) -> tuple:
        version_tuple = parse_version(version_string)
        return super().__new__(cls, version_tuple)

    def __str__(self) -> str:
        return self.raw_value
