from pydantic import BaseModel,  validator
import pandas as pd
import math

class Enquiry(BaseModel):
    Equity: list
    Invested_capital: list

    @validator('Equity', 'Invested_capital')
    def Equity_revenue_(cls, value):
        nw = [float("NaN") if v=='-' else v for v in value]
        nw = [float(i) for i in nw]
        while nw and math.isnan(nw[-1]):
            nw.pop()
        while len(nw) < 10:
            nw = [float('NaN')] + nw
        return [round(item, 2) for item in nw]


def Enquiry_three(content):
    df = pd.read_excel(content)
    Equity = []
    Invested_capital = []
    for row in range(len(df)):
        if 'Return on Equity %' in df.loc[row, 'Fiscal'].strip():
            Equity = df.loc[row].values.tolist()
        if 'Return on Invested Capital %' in df.loc[row, 'Fiscal'].strip():
            Invested_capital = df.loc[row].values.tolist()
    data = Enquiry(Equity=Equity[1:-2], 
                   Invested_capital=Invested_capital[1:-2])
    return data

