# coding: utf-8
import unittest, sys
sys.path.append('../')
from service import CSVHandler
from tests import CSVUtil


class CreditCardRecordTest(unittest.TestCase):
    def setUp(self):
        self.csv_util = CSVUtil()
        self.csv_handler = CSVHandler()
        self.maxDiff=None

    def test_transform_valid_csv_row_into_json(self):
        row = self.csv_util.init_valid_csv_row()
        expected_json_row = self.csv_util.init_valid_csv_json()
        self.assertEqual(expected_json_row, self.csv_handler.transform_csv_row_into_json(row))
    
    def test_transform_invalid_csv_row_into_json(self):
        row = self.csv_util.init_invalid_csv_row()
        expected_json_row = self.csv_util.init_invalid_csv_json()
        self.assertEqual(expected_json_row, self.csv_handler.transform_csv_row_into_json(row))

    def test_transform_empty_csv_row_into_json(self):
        row = self.csv_util.init_empty_csv_json()
        expected_json_row = self.csv_util.init_empty_csv_json()
        self.assertEqual(expected_json_row, self.csv_handler.transform_csv_row_into_json(row))
    
    def test_transform_csv_files_into_json_by_folder(self):
        csv_path = self.csv_util.init_csv_file_path()
        expected_result = self.csv_util.init_list_csv_json()
        self.assertEqual(expected_result, self.csv_handler.transform_csv_files_into_json_by_folder(csv_path))

    def test_transform_csv_files_into_json_by_folder(self):
        csv_path = self.csv_util.init_valid_csv_file_path()
        expected_result = self.csv_util.init_list_csv_json()
        self.assertEqual(expected_result, self.csv_handler.transform_csv_files_into_json_by_folder(csv_path))

    def test_transform_empty_csv_files_into_json_by_folder(self):
        csv_path = self.csv_util.init_empty_csv_file_path()
        expected_result = []
        self.assertEqual(expected_result, self.csv_handler.transform_csv_files_into_json_by_folder(csv_path))

if __name__ == '__main__':
    unittest.main()