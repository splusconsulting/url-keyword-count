# Researches all websites for key word and add we


import urllib2
import csv
import re
from bs4 import BeautifulSoup
import requests
import numpy as np
import socket
from collections import Counter
from urlparse import urlparse

with open('sawmilltest2.csv', 'rb') as dest_f:
    data_iter = csv.reader(dest_f,
                           delimiter = ',',
                           quotechar = '"')
    data = [data for data in data_iter]
data_array = np.asarray(data, dtype = str)
data_array2 = zip(*data_array)

#h = httplib2.Http()
page = list()
links = list()
for url in data_array2[1]:
    req = urllib2.Request(url)
    try:
        html = urllib2.urlopen(req, timeout=5).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all ('a')
        search_word = 'mill'
        matches = re.findall(search_word, html);
        count = Counter (matches)
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    except urllib2.URLError:
        pass
    except socket.timeout:
        pass
    except socket.error:
        pass
    else:
        if len(matches) == 0:
            pass
        else:
            links.append (url + ',' + domain + ',' + search_word + ',' + str(count.values()))
            outputFile = open('output.csv', 'wb')
            outputWriter = csv.writer(outputFile,delimiter=' ')
            for link in links:
                outputWriter.writerow([link])
#print domain
