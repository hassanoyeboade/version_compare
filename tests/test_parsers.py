import unittest

from parameterized import parameterized

from version_compare.parsers import parse_version


class ParseVersionTest(unittest.TestCase):

    @parameterized.expand(
        [
            ("two_parts", "1.3", (1, 3, 0)),
            ("two_parts_with_zero_at_start", "0.3", (0, 3, 0)),
            ("two_parts_with_zero_at_end", "5.0", (5, 0, 0)),
            ("three_parts", "2.3.4", (2, 3, 4)),
            ("three_parts_with_zero_at_start", "0.3.5", (0, 3, 5)),
            ("three_parts_with_zero_at_middle", "35.0.4", (35, 0, 4)),
            ("three_parts_with_zero_at_end", "7.4.0", (7, 4, 0)),
        ]
    )
    def test_value_is_parsed_correctly(self, name, version_string, expected):
        self.assertEqual(parse_version(version_string), expected)
