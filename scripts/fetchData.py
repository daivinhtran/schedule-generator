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
    print(getHeader)
    section = []
    classCode = []

<<<<<<< HEAD
    # Section title
    for i in getHeader:
    	for j in i:
            print(j)
    		# section.append(str(j))
=======
>>>>>>> ca4d4d8ef8e394e7a01fd661e2bec8c007a77646

    trElems = getTable.find_all('tr')
    # print(trElems)
    for tr in trElems:
      # print(tr)
      for i in tr:
        for j in i:
          print(j)

<<<<<<< HEAD
    # print(section)
=======
    # # Section title
    # for i in getHeader:
    # 	for j in i:
    # 		section.append(str(j))

    # # Class code section
    # for ii in getCode:
    #     for code in ii:
    #         code = str(code)
    #         code = re.sub(r"\s+", "", code)
    #         classCode.append(code)

    # print(section)
    # print()
>>>>>>> ca4d4d8ef8e394e7a01fd661e2bec8c007a77646
    # print(classCode)
start('modeling-simulation-information-internetworks')
