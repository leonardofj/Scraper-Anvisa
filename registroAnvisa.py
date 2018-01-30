# -*- coding: utf-8 -*-

import re
import csv
import time
from selenium import webdriver


def pega_dados(browser, url):

	p = dict()
	#p = []

	browser.get(url)
	time.sleep(5)
	#WebDriverWait(browser, 10)

	tabelas = browser.find_elements_by_tag_name('tbody')

	detalhes = tabelas[0].find_elements_by_tag_name('tr')
	#p.append(detalhes[2].find_element_by_tag_name('td').text.encode('utf-8'))
	p[detalhes[2].find_element_by_tag_name('th').text] = detalhes[2].find_element_by_tag_name('td').text.encode('utf-8')

	#p.append(tabelas[1].find_element_by_tag_name('td').text.encode('utf-8'))
	p['modelos'] = tabelas[1].find_element_by_tag_name('td').text.encode('utf-8')

	infos = tabelas[2].find_elements_by_tag_name('tr')
	for info in infos:
		#p.append(info.find_element_by_tag_name('td').text.encode('utf-8'))
	    p[info.find_element_by_tag_name('th').text] = info.find_element_by_tag_name('td').text.encode('utf-8')

	return p


ofile  = open('testAnvisa.csv', "wb")
ofile.write('PRODUTO,NOME TÉCNICO,EMPRESA,NÚMERO DE REGISTRO,ORIGEM DO PRODUTO,CLASSIFICAÇÃO DE RISCO,TIPO DE PROCESSO,NÚMERO DO PROCESSO,RENOVAR ATÉ,VENCIMENTO,MODELOS,STATUS/ RENOVAÇAO,OBSERVAÇÕES\n') 
#.encode('utf-8')

ifile = open('registrosFormed.csv', "rb")
reader = csv.reader(ifile, delimiter=',')
browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
count = 0
for line in reader:
	p = pega_dados(browser, 'https://consultas.anvisa.gov.br/#/saude/' + line[0] + '/?numeroRegistro=' + line[1])
	
	if u'Vencimento do Registro' in p:
		ofile.write("\"%s\",\"%s\",\"\",\"%s\",\"%s\",\"%s\",\"\",\"%s\",\"\",\"%s\",\"%s\"\n" % 
			(p[u'Produto'], p[u'Nome T\xe9cnico'], p[u'Registro'], p[u'Origem do Produto'], p[u'Classifica\xe7\xe3o de Risco'], p[u'Processo'], p[u'Vencimento do Registro'], p['modelos']))
	else:
		ofile.write("\"%s\",\"%s\",\"\",\"%s\",\"%s\",\"%s\",\"\",\"%s\",\"\",\"'cancelado?'\",\"%s\"\n" % 
			(p[u'Produto'], p[u'Nome T\xe9cnico'], p[u'Registro'], p[u'Origem do Produto'], p[u'Classifica\xe7\xe3o de Risco'], p[u'Processo'], p['modelos']))
	count += 1
	print count

ofile.close()
ifile.close()

'''
PRODUTO,
EMPRESA,
NÚMERO DE REGISTRO,
ORIGEM DO PRODUTO,
CLASSIFICAÇÃO DE RISCO,
TIPO DE PROCESSO,
NÚMERO DO PROCESSO,
RENOVAR ATÉ,
VENCIMENTO,
MODELOS,

'''
