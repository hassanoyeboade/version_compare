import unittest

from parameterized import parameterized

from version_compare.version import Version


class VersionTest(unittest.TestCase):
    @parameterized.expand(
        [
            ("two_parts", "1.5", (1, 5, 0)),
            ("two_parts_with_trailing_zero", "1.0", (1, 0, 0)),
            ("two_parts_with_leading_zero", "0.1", (0, 1, 0)),
            ("three_parts", "1.1.4", (1, 1, 4)),
            ("two_parts_with_trailing_zero", "0.1.0", (0, 1, 0)),
            ("three_parts_with_leading_zero", "0.0.1", (0, 0, 1)),
        ]
    )
    def test_instantiation(self, name, version_string, expected):
        version = Version(version_string)
        self.assertEqual(version, expected)
        self.assertEqual(version.raw_value, version_string)

    @parameterized.expand(
        [
            ("two_parts", "3.5"),
            ("two_parts_with_trailing_zero", "4.0"),
            ("two_parts_with_leading_zero", "0.5"),
            ("three_parts", "4.2.3"),
            ("two_parts_with_trailing_zero", "3.4.0"),
            ("three_parts_with_leading_zero", "0.0.4"),
        ]
    )
    def test_string_representation(self, name, version_string):
        version = Version(version_string)
        self.assertEqual(str(version), version_string)
