import unittest
from unittest.mock import patch
from main import PartPicker
from parts import PCParts


class TestPartsByBrand(unittest.TestCase):

    def setUp(self):
        self.part_picker = PartPicker()

    @patch('builtins.input')
    def test_parts_by_brand(self, mock_input):
        parts_list = mock_input.return_value = [
            PCParts("Intel", "Core i9-11900k", 399),
            PCParts("AMD", "Ryzen 9 5900X", 549),
            PCParts("Intel", "Core i7-11700k", 349),
        ]
        result = self.part_picker.get_parts_by_brand(parts_list, "AMD")
        expected_result = ["AMD Ryzen 9 5900X 549"]
        result_brand_model_names = [
            f"{part.get_brand()} {part.get_model()} {part.get_price()}" for part in result]
        self.assertEqual(result_brand_model_names, expected_result)

    @patch('builtins.input')
    def test_if_part_exists_in_parts_list(self, mock_input):
        parts_list = mock_input.return_value = [
            PCParts("Intel", "Core i9-11900k", 399),
            PCParts("Intel", "Core i7-11700k", 349),
        ]
        result = self.part_picker.get_parts_by_brand(
            parts_list, "AMD")
        expected_result = []
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
