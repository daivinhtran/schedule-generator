import requests
from bs4 import BeautifulSoup
import re

def start(thread):
    url = 'http://www.catalog.gatech.edu/programs/' + thread + '-computer-science-bs/#requirementstext'
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    getTable = soup.find(class_='sc_courselist')
    getCode = getTable.find_all('a')
    getHeader = getTable.find_all(class_='courselistcomment areaheader ')
    dict = {}
    section = []
    classCode = []

    # Section title
    for i in getHeader:
    	for j in i:
    		section.append(str(j))

    # Class code section
    for ii in getCode:
        print(ii)
        for code in ii:
            code = str(code)
            code = re.sub(r"\s+", "", code)
            classCode.append(code)

start('modeling-simulation-information-internetworks')
