# coding: utf-8
import sys, json, pandas as pd
sys.path.append('../')
from model import CreditCardRecord

class StatisticsUtil:
    def __init__(self):
        self.record_df = None

    def init_record_df(self):
        data = [["2019","11", "09",271.24, "eletrônicos", "Havan Loja de Deptos", "3", "2"], ["2019", "11", "10", 72.40, "alimentação", "Bistek Supermercados", None, None], ["2019", "11", "11", 21.15, "saúde", "Preço popular farmácias", "2", "1"]]
        self.record_df = pd.DataFrame(data, columns=['year', 'month', 'day', 'amount', 'category', 'store', 'installment_amount', 'installment'])
        return self.record_df

    def init_record_df_grouped_by_category(self):
        data = [["alimentação", 72.40], ["eletrônicos", 271.24], ["saúde", 21.15]]
        self.record_df = pd.DataFrame(data, columns=['category', 'amount'])
        self.record_df.style.hide_index()
        return self.record_df

    def init_reseted_record_df_grouped_by_category(self):
        data = [["alimentação", 0.0], ["eletrônicos", 0.0], ["saúde", 0.0]]
        self.record_df = pd.DataFrame(data, columns=['category', 'amount'])
        self.record_df.style.hide_index()
        return self.record_df

    def init_record_df_grouped_by_month(self):
        data = [["11",  364.79]]
        self.record_df = pd.DataFrame(data, columns=['month', 'amount'])
        self.record_df.style.hide_index()
        return self.record_df

    def init_reseted_record_df_grouped_by_month(self):
        data = [["11",  0.0]]
        self.record_df = pd.DataFrame(data, columns=['month', 'amount'])
        self.record_df.style.hide_index()
        return self.record_df
    
    def init_record_df_grouped_by_year(self):
        data = [["2019",  364.79]]
        self.record_df = pd.DataFrame(data, columns=['year', 'amount'])
        self.record_df.style.hide_index()
        return self.record_df

    def init_reseted_record_df_grouped_by_year(self):
        data = [["2019",  0.0]]
        self.record_df = pd.DataFrame(data, columns=['year', 'amount'])
        self.record_df.style.hide_index()
        return self.record_df