#! Python37
# Sumit Das
# 2019 03 18
# Read EWA reports from folder and show each Files's Section Ratings

from bs4 import BeautifulSoup
import os
import datetime

ALLHTMLfiles = []
EWApath = input("Provide the full path where EWA reports are stored ... :  ")
for HTMLfile in os.listdir(EWApath):
	if HTMLfile.endswith('.htm'):
		ALLHTMLfiles.append(EWApath + "/" + HTMLfile)

DT = datetime.datetime.now()
DateStamp = DT.strftime('%Y-%m-%d_%H-%M-%S')

for EWAfile in ALLHTMLfiles:
	EXF = open(EWAfile, encoding='utf-8')                			# Open a offline HTML file
	EXSOUP = BeautifulSoup(EXF.read(), 'lxml')    	# soup it 
	HEAD = EXSOUP('h1')
	DIV = EXSOUP('div', 'sa-text-level1')
	print("\n ----xxx-----xxx---- \n Ratings from  ", EWAfile, "  \n")
	for i in range(0, len(HEAD)):
		IMG = DIV[i].find('img', alt=True)
		if IMG is not None:
			print(DateStamp, "|", EWAfile, "|", IMG['alt'], "|", HEAD[i].getText())
