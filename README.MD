# web scraping from Morningstar to Excel

## Enquirys:

1) Enquiry 1, from sub-site “Financial Statements” / “Income Statment” 5 Lines / 5 years each + “Fiscal Year ends”, last YEAR and “Currency”
2) Enquiry 2, from sub-site “Financial Statements” / Balance Sheet ” 2 Lines / 5 years each
3) Enquiry 3, from sub-site “Valuations“ / “Operating and Efficiency ” 2 Lines / 10 years each
4) Enquiry 4, from sub-site “Valuations“ / “Financial Health ” 2 Lines / 10 years each
5) Enquiry 5, from sub-site “Valuations“ / “Cash Flow ” 2 Lines / 10 years each
6) Enquiry 6, from sub-site “Dividens” 1 Line / 10 years

# first step 
     create enviroments
        python3 -m venv .venv  linux
        python -m venv .venv windows
        pip install -r requirements.txt
# second step 
     create id.json file I use urls.py 
        pip install playwright
    Install the required browsers:
        playwright install
        - run code
        python urls.py

# last step
    - run code
    python app.py
    in a folder name 'out' will be create morningstar.xlsx


