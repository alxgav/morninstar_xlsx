from pydantic import BaseModel
import pandas as pd
from .moduls import add_to_list


class Enquiry(BaseModel):
    Current_ratio: list
    Book_value: list


def Enquiry_four(content):
    df = pd.read_excel(content)
    Current_ratio = []
    Book_value = []
    for row in range(len(df)):
        if 'Current Ratio' in df.loc[row, 'Liquidity/Financial Health']:
            Current_ratio = df.loc[row].values.tolist()
        if 'Book Value/Share' in df.loc[row, 'Liquidity/Financial Health']:
            Book_value = df.loc[row].values.tolist()
    return Enquiry(Current_ratio=add_to_list(Current_ratio[1:-1], 10), 
                   Book_value=add_to_list(Book_value[1:-1], 10),
                       )