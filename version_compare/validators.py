import re


version_regex_patter = r'^\d+(\.\d+){1,2}$'
version_regex_error_message = '"{version}" must be of format "a.b" or "a.b.c" where a, b and c are positive integers'


def validate_version(version: str) -> str:
    """
    Validate version to be of correct format
    :param version: version to be validated
    :return: validated version
    :raises ValueError if version is not valid
    """

    if re.match(version_regex_patter, version) is None:
        raise ValueError(version_regex_error_message.format(version=version))

    if all(int(part) == 0 for part in version.split('.')):
        raise ValueError('minimum expected version is "0.0.1"')

    return version
