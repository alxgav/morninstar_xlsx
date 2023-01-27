from pydantic import BaseModel,  validator
import pandas as pd
from .moduls import add_to_list


class Enquiry(BaseModel):
    Total_assest: list
    Total_equity: list

    @validator('Total_assest', 'Total_equity')
    def Total_assest_(cls, value):
        return [round(item, 2)/1000000 for item in value]

def Enquiry_two(content):
    df = pd.read_excel(content)
    headers = df.columns.tolist()
    Total_assest = []
    Total_equity = []
    for row in range(len(df)):
        if 'Total Assets' in df.loc[row, headers[0]]:
            Total_assest = df.loc[row].values.tolist()
        if 'Total Equity' in df.loc[row, headers[0]]:
            Total_equity = df.loc[row].values.tolist()
    
    return Enquiry(Total_assest=add_to_list(Total_assest[1:], 5), 
                   Total_equity=add_to_list(Total_equity[1:], 5),
                       )