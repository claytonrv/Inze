import pandas as pd 
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

class  RecordStatisticsHandler:
    def __init__(self):
        self.record_df = None

    def converRecordsToDf(self, record_list):
        try:
            self.record_df = pd.DataFrame.from_records([r.to_dict() for r in record_list])
        except:
            self.record_df = None
        return self.record_df
    
    def group_df_data_by_category(self, record_df):
        categories_df = record_df.groupby('category')['amount'].sum().reset_index()
        categories_df.amount = [round(x, 2) for x in categories_df.amount]
        return categories_df
    
    def group_df_data_by_month(self, record_df):
        month_df = record_df.groupby('month')['amount'].sum().reset_index()
        month_df.amount = [round(x, 2) for x in month_df.amount]
        return month_df 

    def group_df_data_by_year(self, record_df):
        year_df = record_df.groupby('year')['amount'].sum().reset_index()
        year_df.amount = [round(x, 2) for x in year_df.amount]
        return year_df

