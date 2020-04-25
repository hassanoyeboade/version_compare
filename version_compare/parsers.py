from typing import Tuple


TUPLE_LENGTH = 3


def parse_version(version: str) -> Tuple:
    """
    Parse version string into a 3-tuple of ints
    :param version: A string representing the first version
    :return: A 3-tuple of ints representing the version

    Examples::
        parse_version_string("1.3") => (1, 3, 0)
        parse_version_string("0.9.9") => (0, 9, 9)
        parse_version_string("5.11.9") => (5, 11, 9)
    """

    version_tuple = tuple(map(int, version.split(".")))

    # Fill the tuple with 0s if less than required tuple length
    version_tuple = version_tuple + ((0,) * (TUPLE_LENGTH - len(version_tuple)))

    return version_tuple
