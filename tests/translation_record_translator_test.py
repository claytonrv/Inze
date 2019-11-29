# coding: utf-8
import unittest, sys, json
sys.path.append('../')
from translation import RecordTranslator
from tests import RecordUtil

class CreditCardRecordTest(unittest.TestCase):
    def setUp(self):
        self.record_util = RecordUtil()
        self.record_translator = RecordTranslator()
        self.maxDiff = None

    def test_recordToJsonTest(self):
        record = self.record_util.initValidRecord()
        expected_record_json = self.record_util.initRecordJson()
        expected_record_json = self.record_util.initRecordJson()
        self.assertEqual(self.record_translator.translate_record_to_json(record), expected_record_json)

    def test_noneRecordToJsonTest(self):
        record = self.record_util.initInvalidRecord()
        record_json = self.record_util.initInvalidRecordJson()
        self.assertEqual(self.record_translator.translate_record_to_json(record).strip(), record_json.strip())

    def test_emptyRecordToJsonTest(self):
        record = self.record_util.initEmptyRecord()
        record_json = self.record_util.initEmptyRecordJson()
        self.assertEqual(self.record_translator.translate_record_to_json(record).strip(), record_json.strip())

    def test_recordListToJson(self):
        json_record_list = []
        rec_list = self.record_util.initValidRecordList()
        for record in rec_list:
            rec = self.record_translator.translate_record_to_json(record)
            json_record_list.append(rec)
        expected_json_record_list = self.record_util.initRecordJsonList()
        self.assertEqual(self.record_translator.translate_record_list_to_json_list(json_record_list), expected_json_record_list)

if __name__ == '__main__':
    unittest.main()