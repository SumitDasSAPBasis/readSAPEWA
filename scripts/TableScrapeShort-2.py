import pandas as pd
import os

# url = r'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
url = r'https://raw.githubusercontent.com/RustyNails8/readSAPEWA/RustyNails8-upload-sampleEWA/P6E.htm'

tables = pd.read_html(url) # Returns list of all tables on page
#print(tables)

# sp500_table = tables[0] # Select table of interest
for table_of_interest in tables:
    print(table_of_interest)
    os.system("pause")


# print(sp500_table)

# https://stackoverflow.com/questions/6325216/parse-html-table-to-python-list