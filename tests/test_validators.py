import unittest

from parameterized import parameterized

from version_compare.validators import validate_version


class ValidateVersionTest(unittest.TestCase):

    @parameterized.expand(
        [
            ("one_part", "0",),
            ("one_part_with_trailing_dot", "1.",),
            ("one_part_with_multiple_trailing_dots", "9....",),
            ("one_part_with_leading_dot", ".2",),
            ("one_part_with_multiple_leading_dots", "....3",),
            ("one_part_with_leading_and_trailing_dot", ".5.",),
            ("one_part_with_multiple_leading_and_trailing_dots", "...0....",),
            ("one_part_non_integer", "a",),
            ("two_parts_with_trailing_dot", "1.3.",),
            ("two_parts_with_multiple_trailing_dots", "0.3....",),
            ("two_parts_with_leading_dot", ".2.6",),
            ("two_parts_with_multiple_leading_dots", "...8.5",),
            ("two_parts_with_leading_and_trailing_dot", ".3.6.",),
            ("two_parts_with_multiple_leading_and_trailing_dots", "...3.6...",),
            ("two_parts_non_integer", "g.h",),
            ("three_parts_with_trailing_dot", "1.3.9.",),
            ("three_parts_with_multiple_trailing_dots", "0.3.8....",),
            ("three_parts_with_leading_dot", ".2.6.7",),
            ("three_parts_with_multiple_leading_dots", "...8.5.8",),
            ("three_parts_with_leading_and_trailing_dot", ".3.6.7.",),
            ("three_parts_with_multiple_leading_and_trailing_dots", "...0.3.6...",),
            ("three_parts_non_integer", "g.h.$",),
        ]
    )
    def test_when_version_is_not_expected_format(self, name, version_string):
        with self.assertRaises(ValueError):
            self.assertRaises(validate_version(version_string))

    @parameterized.expand(
        [
            ("two_parts", "0.0",),
            ("three_parts", "0.0.0",),
        ]
    )
    def test_when_version_parts_is_all_zero(self, name, version_string):
        with self.assertRaises(ValueError):
            self.assertRaises(validate_version(version_string))
