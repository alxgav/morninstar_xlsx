from pydantic import BaseModel,  validator
import pandas as pd
from .moduls import add_to_list
from pprint import pprint




class Enquiry(BaseModel):
    Total_revenue: list
    Diluted_net: list
    Diluted_weighted: list
    Diluted_ESP: list
    Year_end_month: str
    Year_end: str
    currency: str

    @validator('Year_end')
    def Year_end_(cls, v):
        if v is None:
            return 'no data'
        return v
    

    @validator('Total_revenue', 'Diluted_net', 'Diluted_weighted')
    def Total_revenue_(cls, value):
        return [round(float(item), 2)/1000000 for item in value]

def Enquiry_one(content):
    month = (('Jan', '01'), 
             ('Feb', '02'),
             ('Mar', '03'),
             ('Apr', '04'),
             ('May', '05'),
             ('Jun', '06'),
             ('Jul', '07'),
             ('Aug', '08'),
             ('Sep', '09'),
             ('Oct', '10'),
             ('Nov', '11'),
             ('Dec', '12'))
    Total_revenue = []
    Diluted_net = []
    Diluted_weighted = []
    Diluted_ESP = []
    df = pd.read_excel(content)
    headers = df.columns.tolist()
    for row in range(len(df)):
        if 'Total Revenue' == df.loc[row, headers[0]].strip():
            Total_revenue = df.loc[row].values.tolist()
        if 'Diluted Net Income Available to Common Stockholders' == df.loc[row, headers[0]].strip():
            Diluted_net = df.loc[row].values.tolist()
        if len(Diluted_net) == 0:
            if 'Net Income Available to Common Stockholders' == df.loc[row, headers[0]].strip():
                Diluted_net = df.loc[row].values.tolist()
        if 'Diluted Weighted Average Shares Outstanding' == df.loc[row, headers[0]].strip():
            Diluted_weighted = df.loc[row].values.tolist() 
        if 'Diluted EPS' == df.loc[row, headers[0]].strip():
            Diluted_ESP = df.loc[row].values.tolist()
    last_row = df.iloc[-1].values.tolist()[0].split('|')
    last_year = df.columns.tolist()[-2]
    Year_end_month = last_row[0].split('in')[1].split()[0]
    for month in month:
        if Year_end_month in month:
            Year_end_month = month[1]
    data = Enquiry(Total_revenue=add_to_list(Total_revenue[1:-1], 5), 
                    Diluted_net=add_to_list(Diluted_net[1:-1], 5),
                    Diluted_weighted=add_to_list(Diluted_weighted[1:-1], 5),
                    Diluted_ESP=add_to_list(Diluted_ESP[1:-1], 5),
                    Year_end_month=Year_end_month,
                    Year_end=last_year,
                    currency=last_row[1])
    return data