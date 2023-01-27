from pydantic import BaseModel
import pandas as pd
from .moduls import add_to_list


class Enquiry(BaseModel):
    capExAsPerOfSales: list
    freeCashFlowPerShare: list


def Enquiry_five(content):
    df = pd.read_excel(content)
    capExAsPerOfSales = []
    freeCashFlowPerShare = []
    for row in range(len(df)):
        if 'Cap Ex as a % of Sales' in df.loc[row, 'Cash Flow Ratios']:
            capExAsPerOfSales = df.loc[row].values.tolist()
        if 'Free Cash Flow/Share' in df.loc[row, 'Cash Flow Ratios']:
            freeCashFlowPerShare = df.loc[row].values.tolist()
    
    
    return Enquiry(capExAsPerOfSales=add_to_list(capExAsPerOfSales[1:-1], 10), 
                   freeCashFlowPerShare=add_to_list(freeCashFlowPerShare[1:-1], 10),
                       )