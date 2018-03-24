import requests
from bs4 import BeautifulSoup
import re
import json


def start():
    url = 'http://www.catalog.gatech.edu/programs/computer-science-bs/#threadstext'
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    getTable = soup.find(id='threadstextcontainer')
    getHeader = getTable.find_all('h3')
    getBranch = getTable.find_all('li')
    threads = []
    threadss = {
        "Devices": [],
        "Infor InternetWorks": [],
        "Intelligence": [],
        "Media":[],
        "People":[],
        "Modeling and Simulation": [],
        "Systems and Architecture": [],
        "Theory": []
    }

    # Get all threads
    for i in getHeader:
        for j in i:
            threads.append(str(j))

    # Get all final threads:
    for i in getBranch:
        for j in i:
            for jj in j:
                # thread = jj.lower()
                # thread = re.sub('&', "", thread)
                # thread = re.sub('and', "", thread)
                # thread = re.sub(r"\s+", "-", thread)
                if ('& Devices' in jj):
                    threadss['Devices'].append(jj) 
                elif ('& Information Internetworks' in jj):
                    threadss['Infor InternetWorks'].append(jj)
                elif ('& Intelligence' in jj):
                    threadss['Intelligence'].append(jj)
                elif ('& Media' in jj):
                    threadss['Media'].append(jj)
                elif ('& Modeling and Simulation' in jj):
                    threadss['Modeling and Simulation'].append(jj)
                elif ('& People' in jj):
                    threadss['People'].append(jj)
                elif ('& Systems and Architecture' in jj):
                    threadss['Systems and Architecture'].append(jj)
                elif ('& Theory' in jj):
                    threadss['Theory'].append(jj)


    # Save to json file
    threadss = json.dumps(threadss)
    f = open("threads.json","w")
    f.write(threadss)
    f.close()
