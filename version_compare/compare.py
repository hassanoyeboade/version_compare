from .version import Version


def compare_versions(version_1: str, version_2: str) -> str:
    """
    Compares two version strings and returns whether one is greater than, equal, or less than the other.
    As an example: "1.2" is greater than "1.1", "1.3" is equal to "1.3", "1.4" is less than 1.5.
    Version strings are of format "a.b" or "a.b.c" where a, b and c are positive integers
    :param version_1: A string representing the first version
    :param version_2: A string representing the second version
    :return: string representing the result of comparison

    Examples::
        check_version("1.2", "1.3") => "1.2" is less than "1.3"
        check_version("1.2", "1.2.0") => "1.2" is equal to "1.2.0"
        check_version("1.3", "1.3.5") => "1.3" is less than "1.3.5"
        check_version("1.4", "1.3") => "1.4" is greater than "1.3"
        check_version("1.5", "1.2.1") => "1.5" is greater than "1.2.1"
    """

    version_1 = Version(version_1)
    version_2 = Version(version_2)

    if version_1 == version_2:
        return f'"{version_1}" is equal to "{version_2}"'

    if version_1 > version_2:
        return f'"{version_1}" is greater than "{version_2}"'

    if version_1 < version_2:
        return f'"{version_1}" is less than "{version_2}"'
