# Researches all websites for key word and add website and


import urllib2
import csv
import re
from bs4 import BeautifulSoup
import requests
import numpy as np
import socket
from collections import Counter
from urlparse import urlparse

with open('resellers.csv', 'rb') as dest_f:
    data_iter = csv.reader(dest_f,
                           delimiter = ',',
                           quotechar = '"')
    data = [data for data in data_iter]
data_array = np.asarray(data, dtype = str)
data_array2 = zip(*data_array)

#h = httplib2.Http()
page = list()
links = list()

url_ingore = ['http://www.yellowpages.com/', 'https://en.wikipedia.org/', 'https://www.youtube.com/', 'http://www.manta.com/', 'http://www.bbb.org/', 'http://www.bloomberg.com/']

for url in data_array2[1]:
    req = urllib2.Request(url)
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    if domain in url_ingore:
        pass
    else:
        try:
            html = urllib2.urlopen(req, timeout=5).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup.find_all ('a')
            search_word = 'Metalworking'
            search_word2 = 'Lubricant'
            search_word3 = 'Grease'
            search_word4 = 'Industrial'
            search_word5 = 'Hydraulic'
            matches = re.findall(search_word, html);
            matches2 = re.findall(search_word2, html);
            matches3 = re.findall(search_word3, html);
            matches4 = re.findall(search_word4, html);
            matches5 = re.findall(search_word4, html);
            count = Counter (matches)
            count2 = Counter (matches2)
            count3 = Counter (matches3)
            count4 = Counter (matches4)
            count5 = Counter (matches5)
        except urllib2.URLError:
            pass
        except socket.timeout:
            pass
        except socket.error:
            pass
        else:
            if len(matches) + len(matches2) + len(matches3) + len(matches4) + len(matches4) == 0:
                pass
            else:
                links.append (url + ',' + domain + ',' + search_word + ',' + str(count.values()) + ',' + search_word2 + ',' + str(count2.values())
                + ',' + search_word3 + ',' + str(count3.values()) + ',' + search_word4 + ',' + str(count4.values()) + ',' + search_word5 + ',' + str(count5.values()))
                outputFile = open('reseller_output.csv', 'wb')
                outputWriter = csv.writer(outputFile,delimiter=' ')
                for link in links:
                    outputWriter.writerow([link])
    #print domain
