from pydantic import BaseModel, validator


class Enquiry(BaseModel):
    Dividend_Per_Share: list

    @validator('Dividend_Per_Share')
    def Dividend_Per_Share_(cls, value):
        nw = [float("NaN") if v is None else v for v in value]
        return [round(float(item), 2) for item in nw ]

def Enquiry_six(response):
    Dividend_Per_Share = []
    for row in response['rows']:
        if row['label'] == 'Dividend Per Share':
            Dividend_Per_Share = row['datum']
    data = Enquiry(Dividend_Per_Share=Dividend_Per_Share[:-3])
    return data