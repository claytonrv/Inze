# coding: utf-8
import unittest, sys
sys.path.append('../')
from tests import RecordUtil, StatisticsUtil
from statistics import RecordStatisticsHandler

class RecordStatisticsHandlerTest(unittest.TestCase):
    def setUp(self):
        self.maxDiff=None

    def test_record_list_to_df_conversio(self):
        record_list = RecordUtil().initValidRecordList()
        returned_value = RecordStatisticsHandler().converRecordsToDf(record_list)
        expected_value = StatisticsUtil().init_record_df()
        self.assertTrue(expected_value.equals(returned_value))

    def test_invalid_record_list_to_df_conversio(self):
        record_list = RecordUtil().initInvalidRecordList()
        returned_value = RecordStatisticsHandler().converRecordsToDf(record_list)
        expected_value = StatisticsUtil().init_record_df()
        print(returned_value)
        self.assertEquals(None, returned_value)
    
    def test_data_group_by_category(self):
        record_list = RecordUtil().initValidRecordList()
        handler = RecordStatisticsHandler()
        records_df = handler.converRecordsToDf(record_list)
        expected_value = StatisticsUtil().init_record_df_grouped_by_category()
        returned_value = handler.group_df_data_by_category(records_df)
        self.assertTrue(returned_value.equals(expected_value))

    def test_reseted_data_group_by_category(self):
        record_list = RecordUtil().initNoAmountRecordList()
        handler = RecordStatisticsHandler()
        records_df = handler.converRecordsToDf(record_list)
        expected_value = StatisticsUtil().init_reseted_record_df_grouped_by_category()
        returned_value = handler.group_df_data_by_category(records_df)
        self.assertTrue(returned_value.equals(expected_value))

    def test_data_group_by_month(self):
        record_list = RecordUtil().initValidRecordList()
        handler = RecordStatisticsHandler()
        records_df = handler.converRecordsToDf(record_list)
        expected_value = StatisticsUtil().init_record_df_grouped_by_month()
        returned_value = handler.group_df_data_by_month(records_df)
        self.assertTrue(returned_value.equals(expected_value))
    
    def test_reseted_data_group_by_month(self):
        record_list = RecordUtil().initNoAmountRecordList()
        handler = RecordStatisticsHandler()
        records_df = handler.converRecordsToDf(record_list)
        expected_value = StatisticsUtil().init_reseted_record_df_grouped_by_month()
        returned_value = handler.group_df_data_by_month(records_df)
        self.assertTrue(returned_value.equals(expected_value))

    def test_data_group_by_year(self):
        record_list = RecordUtil().initValidRecordList()
        handler = RecordStatisticsHandler()
        records_df = handler.converRecordsToDf(record_list)
        expected_value = StatisticsUtil().init_record_df_grouped_by_year()
        returned_value = handler.group_df_data_by_year(records_df)
        self.assertTrue(returned_value.equals(expected_value))

    def test_data_group_by_year(self):
        record_list = RecordUtil().initNoAmountRecordList()
        handler = RecordStatisticsHandler()
        records_df = handler.converRecordsToDf(record_list)
        expected_value = StatisticsUtil().init_reseted_record_df_grouped_by_year()
        returned_value = handler.group_df_data_by_year(records_df)
        self.assertTrue(returned_value.equals(expected_value))