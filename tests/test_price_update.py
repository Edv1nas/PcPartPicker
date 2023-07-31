import unittest
from unittest.mock import patch
from main import PartPicker
from parts import PCParts


class TestPriceUpdate(unittest.TestCase):

    def setUp(self):
        self.part_picker = PartPicker()

    @patch('builtins.input')
    def test_price_update(self, mock_input):
        parts_list = mock_input.return_value = [
            PCParts("Corsair", "Vengeance LPX", 39.99),
            PCParts("G.Skill", "Trident Z5 RGB", 224.99),
            PCParts("Silicon", "Power GAMING", 29.97),
        ]
        result = self.part_picker.update_price(
            parts_list, "Corsair", "Vengeance LPX", 100.99)
        expected_result = True
        self.assertEqual(result, expected_result)

    @patch('builtins.input')
    def test_if_part_not_found(self, mock_input):
        parts_list = mock_input.return_value = [
            PCParts("Corsair", "Vengeance LPX", 39.99),
            PCParts("G.Skill", "Trident Z5 RGB", 224.99),
            PCParts("Silicon", "Power GAMING", 29.97)
        ]
        result = self.part_picker.update_price(
            parts_list, "Msi", "MAG B660 TOMAHAWK WIFI", 29.97)
        expected_result = False
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
