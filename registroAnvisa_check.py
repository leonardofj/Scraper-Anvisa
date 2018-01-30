# -*- coding: utf-8 -*-

import csv
from selenium import webdriver


ifile = open('registrosFormed.csv', "rb")
reader = csv.reader(ifile, delimiter=',')
browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
count = 0
url = ''
for line in reader:
	url = 'https://consultas.anvisa.gov.br/#/saude/' + line[0] + '/?numeroRegistro=' + line[1]
	browser.get(url)
	count += 1
	print count
	raw_input(u'Next...')

ifile.close()

