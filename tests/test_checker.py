import unittest

from parameterized import parameterized

from version_compare.compare import compare_versions


class VersionCheckerIntegrationTest(unittest.TestCase):
    @parameterized.expand(
        [
            ("start_with_zero_and_equal", "0.5", "0.5", '"0.5" is equal to "0.5"'),
            ("start_with_zero_and_greater_than", "0.9", "0.8", '"0.9" is greater than "0.8"'),
            ("start_with_zero_and_less_than", "0.1", "0.6", '"0.1" is less than "0.6"'),
            ("end_with_zero_and_equal", "1.0", "1.0", '"1.0" is equal to "1.0"'),
            ("end_with_zero_and_greater_than", "2.0", "1.0", '"2.0" is greater than "1.0"'),
            ("end_with_zero_land_ess_than", "1.0", "3.0", '"1.0" is less than "3.0"'),
            ("doesnt_contain_zero_and_equal", "1.2", "1.2", '"1.2" is equal to "1.2"'),
            ("doesnt_contain_zero_and_greater_than", "3.4", "1.2", '"3.4" is greater than "1.2"',),
            ("doesnt_contain_zero_and_less_than", "4.5", "5.6", '"4.5" is less than "5.6"'),
        ]
    )
    def test_when_versions_consist_of_two_parts(
        self, name, version_1, version_2, expected
    ):
        self.assertEqual(compare_versions(version_1, version_2), expected)

    @parameterized.expand(
        [
            ("start_with_zero_and_equal", "0.3.6", "0.3.6", '"0.3.6" is equal to "0.3.6"'),
            ("start_with_zero_and_greater_than", "0.9.3", "0.8.10", '"0.9.3" is greater than "0.8.10"'),
            ("start_with_zero_and_less_than", "0.1.3", "0.6.9", '"0.1.3" is less than "0.6.9"'),
            ("end_with_zero_and_equal", "1.0.0", "1.0.0", '"1.0.0" is equal to "1.0.0"'),
            ("end_with_zero_and_greater_than", "2.0.0", "1.0.0", '"2.0.0" is greater than "1.0.0"'),
            ("end_with_zero_and_less_than", "1.4.0", "3.3.0", '"1.4.0" is less than "3.3.0"'),
            ("zero_in_middle_and_equal", "1.0.4", "1.0.4", '"1.0.4" is equal to "1.0.4"'),
            ("zero_in_middle_and_greater_than", "2.0.1", "1.0.5", '"2.0.1" is greater than "1.0.5"'),
            ("zero_in_middle_and_less_than", "5.0.9", "5.0.10", '"5.0.9" is less than "5.0.10"'),
            ("doesnt_contain_zero_and_equal", "1.2.1", "1.2.1", '"1.2.1" is equal to "1.2.1"'),
            ("doesnt_contain_zero_and_greater_than", "3.4.5", "1.2.2", '"3.4.5" is greater than "1.2.2"',),
            ("doesnt_contain_zero_and_less_than", "4.2.5", "8.5.116", '"4.2.5" is less than "8.5.116"'),
        ]
    )
    def test_when_versions_consist_of_three_parts(
            self, name, version_1, version_2, expected
    ):
        self.assertEqual(compare_versions(version_1, version_2), expected)

    @parameterized.expand(
        [
            ("equal", "0.3", "0.3.0", '"0.3" is equal to "0.3.0"'),
            ("greater_than", "0.7.3", "0.5", '"0.7.3" is greater than "0.5"'),
            ("less_than", "2.9", "4.9.10", '"2.9" is less than "4.9.10"'),
        ]
    )
    def test_when_versions_consist_of_two_and_three_parts(
            self, name, version_1, version_2, expected
    ):
        self.assertEqual(compare_versions(version_1, version_2), expected)

    @parameterized.expand(
        [
            ("version_1_two_parts", "0.0", "0.4"),
            ("version_2_two_parts", "0.4", "0.0"),
            ("version_1_three_parts", "0.0.0", "0.4"),
            ("version_2_three_parts", "4.4", "0.0.0"),
            ("version_1_three_parts", "0.0.0", "0.0.4"),
            ("version_2_three_parts", "3.0.0", "0.0.0"),
            ("version_1_two_parts_and_version_2_three_parts", "0.0", "0.0.0"),
            ("version_1_three_parts_and_version_2_two_parts", "0.0.0", "0.0"),
        ]
    )
    def test_when_version_parts_is_all_zero(self, name, version_1, version_2):
        with self.assertRaises(ValueError):
            self.assertRaises(compare_versions(version_1, version_2))
