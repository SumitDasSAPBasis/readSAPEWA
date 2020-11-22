#! Python37
# Sumit Das
# 2019 03 19
# Read EWA reports from folder and show each Files's Section Ratings

from bs4 import BeautifulSoup
import os
import datetime
import csv

DT = datetime.datetime.now()
DateStamp = DT.strftime('%Y-%m-%d_%H-%M-%S')
CSVpath = input("Provide the full path where CSV reports shall be stored ... :  ")
CSVfile = "ConsolidateEWArating_%s.CSV" % DateStamp
OutCSV = open(CSVpath + "/" + CSVfile, 'w', newline='')
OutWriter = csv.writer(OutCSV)

ALLHTMLfiles = []
EWApath = input("Provide the full path where EWA reports are stored ... :  ")
for HTMLfile in os.listdir(EWApath):
	if HTMLfile.endswith('.htm'):
		ALLHTMLfiles.append(EWApath + "/" + HTMLfile)

for EWAfile in ALLHTMLfiles:
	EXF = open(EWAfile)                			    # Open a offline HTML file
	EXSOUP = BeautifulSoup(EXF.read(), 'lxml')    	# soup it 
	HEAD = EXSOUP('h1')
	DIV = EXSOUP('div', 'sa-text-level1')

	print("\n ----xxx-----xxx---- \n Ratings from  ", EWAfile, "  \n")

	for i in range(0, len(HEAD)):
		IMG = DIV[i].find('img', alt=True)
		if IMG is not None:
			print(DateStamp, "|", EWAfile, "|", IMG['alt'], "|", HEAD[i].getText())
			IMGsplit = IMG['alt'].split(' ')
			IMGcsv = IMGsplit[0]
			EWAfileSPLIT = EWAfile.split('_')
			EWAfileSPLIT
			EWAfileSID = EWAfileSPLIT[0]
			EWAfileRATING = EWAfileSPLIT[1]
			# EWAfileWEEKhtm = EWAfileSPLIT[3].split('.')
			# EWAfileWEEK = EWAfileWEEKhtm[0]


			headCSV = HEAD[i].getText()

			OutWriter.writerow([DateStamp, EWAfileSID, EWAfileRATING, IMGcsv, headCSV])

OutCSV.close()
