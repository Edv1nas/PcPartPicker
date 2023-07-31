import unittest
from unittest.mock import patch
from main import PartPicker
from parts import PCParts


class TestReadParts(unittest.TestCase):

    def setUp(self):
        self.part_picker = PartPicker()

    @patch('builtins.input')
    def test_read_parts(self, mock_input):
        parts_list = mock_input.return_value = [
            PCParts("Msi", "MAG B660 TOMAHAWK WIFI", 189.99),
            PCParts("Gigabyte", "Z790 AORUS ELITE AX", 249.99),
            PCParts("Msi", "B550M PRO-VDH WIFI", 119.99),
        ]
        result = self.part_picker.read_parts(
            parts_list, "Msi", "MAG B660 TOMAHAWK WIFI")
        expected_result = ["Msi MAG B660 TOMAHAWK WIFI"]
        result_brand_model_names = [
            f"{part.get_brand()} {part.get_model()}" for part in result]
        self.assertEqual(result_brand_model_names, expected_result)

    @patch('builtins.input')
    def test_if_part_not_found_with_specified_brand_and_model(self, mock_input):
        parts_list = mock_input.return_value = [
            PCParts("Intel", "Core i9-11900k", 399),
            PCParts("Intel", "Core i7-11700k", 349),
        ]
        result = self.part_picker.read_parts(
            parts_list, "Msi", "MAG B660 TOMAHAWK WIFI")
        expected_result = []
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
