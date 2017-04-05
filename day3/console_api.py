
'''API for requesting books when given the authors name
    Im using Goodreads.com to make my requests
    An API key is required which i obtained by logging in
    Import the xml dom for parsing since the api will respond in xml format'''
# -*- coding: utf-8 -*-
import urllib3
from xml.dom import minidom

#make a request using pool manager
conn=urllib3.PoolManager()

#define a function that takes an authours name
def find_book_by_author(author):
#key is required by the api
    api_key="zP9LAJl2GjZfNRjS7bKyg"
#replace the spaces between names with %20
    author_name=author.replace(' ','%20')
#obtain the final url to be requested
    url="https://www.goodreads.com/search/index.xml?key="+api_key+ "&q=" +author_name
#open a connection to the url
    obj = conn.urlopen('GET', url)
#parse the http response
    parser = minidom.parseString(obj.data)
    Titles = parser.getElementsByTagName('title')
#iterate through each one to display one book title at a time
    for title in Titles:
            print("The Book is Titled "+ title.firstChild.nodeValue)



##SOME NAMES YOU CAN TEST WITH
#dan brown
#willian shakespeare
#robert jackson
#orson scott
#carolyn keene
#etc
