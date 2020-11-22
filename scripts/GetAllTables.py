import pandas as pd
import os
import pandas as pds

pds_df = pds.read_html('data/P6E.htm')

table_no = 0
for table_of_interest in pds_df:
    print("###########################")
    print("Table number:  ", table_no)
    print("---------------------------")
    print(table_of_interest)
    print("                ")
    os.system("pause")
    print("---------------------------")
    print("###########################")
    table_no = table_no + 1


#https://stackoverflow.com/questions/6325216/parse-html-table-to-python-list

""" # url = r'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
url = r'https://raw.githubusercontent.com/RustyNails8/readSAPEWA/RustyNails8-upload-sampleEWA/P6E.htm'

tables = pd.read_html(url) # Returns list of all tables on page
#print(tables)

# sp500_table = tables[0] # Select table of interest
for table_of_interest in tables:
    print(table_of_interest)
    os.system("pause")


# print(sp500_table)

# https://stackoverflow.com/questions/6325216/parse-html-table-to-python-list """