import unittest

from ddt import ddt, data, unpack

from helper import is_repeating
from helper import remove_first_occurrence_of_character
from helper import remove_given_character
from helper import repeating_to_single_string_converter


@ddt
class TestStringMethods(unittest.TestCase):

    @data(["TechCity", "Techiy"], ["TechTeam", "Techam"], ["Umbrella", "Umbrela"], ["Data", "Dat"], ["Google", "Gole"])
    @unpack
    def test_repeating_to_single_string_converter(self, input_value, output_value):
        self.assertTrue(repeating_to_single_string_converter(input_value) == output_value)

    @data(["TechCity", "c"], ["TechCity", "C"], ["Umbrella", "L"], ["Data", "a"])
    @unpack
    def test_is_repeating(self, input_value1, input_value2):
        self.assertTrue(is_repeating(input_value1, input_value2))

    @data(["TechCity", "T", "echCity"], ["TechTeam", "m", "TechTea"], ["Umbrella", "e", "Umbrlla"])
    @unpack
    def test_remove_given_character(self, input_value1, input_value2, output_value):
        self.assertEqual(remove_given_character(input_value1, input_value2), output_value)

    @data(["TechCity", "ehCity"], ["TechTeam", "chTeam"], ["Umbrella", "Umbrela"], ["Data", "Dta"], ["Google", "ogle"])
    @unpack
    def test_remove_first_occurence_of_character(self, input_value, output_value):
        self.assertEqual(remove_first_occurrence_of_character(input_value), output_value)


if __name__ == "__main__":
    unittest.main()
