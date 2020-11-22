#! python
# Sumit Das 18-MAR-2019
# Get ALL Rating in 1 EWA file
# Sumit Das 22-NOV-2020

from bs4 import BeautifulSoup

EXF = open('data/P6E.htm')                # Open a offline HTML file
EXSOUP = BeautifulSoup(EXF.read(), 'lxml')    # soup it 
LISTS = EXSOUP.select('div li')       # Collect all elements of

"""
for i in range(0, len(lists)) :       # See all elements
    lists[i].getText()
    i += 1

for DIV in EXSOUP.find_all('div', 'sa-text-level1') :  # Find div with class
    for IMG in DIV.find_all('img', alt = True) :       # Find img in div
        print(IMG['alt'])                              # Print only the alt
"""

HEAD1 = EXSOUP('h1')
DIV1 = EXSOUP('div', 'sa-text-level1')

print("\n")
for i in range(0, len(HEAD1)):
    IMG1 = DIV1[i].find('img', alt=True)
    if IMG1 is not None:
        print(IMG1['alt'], "||", HEAD1[i].getText())
