import unittest
from unittest.mock import patch
from main import PartPicker
from parts import PCParts


class TestViewParts(unittest.TestCase):

    def setUp(self):
        self.part_picker = PartPicker()

    @patch('builtins.input')
    def test_view_parts(self, mock_input):
        parts_list = mock_input.return_value = [
            PCParts("Intel", "Core i9-11900k", 399),
            PCParts("AMD", "Ryzen 9 5900X", 549),
            PCParts("Intel", "Core i7-11700k", 349),
        ]
        result = self.part_picker.view_all_parts(parts_list)
        expected_result = [
            "Intel Core i9-11900k - Price: 399",
            "AMD Ryzen 9 5900X - Price: 549",
            "Intel Core i7-11700k - Price: 349"
        ]
        result_brand_model_prices = [
            f"{part.get_brand()} {part.get_model()} - Price: {part.get_price()}" for part in result
        ]
        self.assertEqual(result_brand_model_prices, expected_result)

    @patch('builtins.input')
    def test_if_parts_list_is_empty(self, mock_input):
        parts_list = mock_input.return_value = []
        result = self.part_picker.view_all_parts(parts_list)
        expected_result = []
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
