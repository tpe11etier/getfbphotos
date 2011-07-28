#!/usr/bin/env python

import httplib
import json
import urllib
from urllib import urlretrieve
from urllib import urlopen
from urlparse import urlparse


server = 'graph.facebook.com'
myID = 'tpe11etier'
accessToken = '219829968059223|2.AQCNSrupRACnjhKJ.3600.1311868800.0-1015377839|mmgdXr_PrqvNWdPfPZ5wUufgk2c'
URL = "/tpe11etier/friends?access_token=" + accessToken

def getfriends():
    conn = httplib.HTTPSConnection(server)
    conn.request("GET", URL)
    response = conn.getresponse()
    data = response.read()
    list = json.loads(data)['data']
    IDs = [(friends['id'], friends['name']) for friends in list]
    return IDs


def getphotos():
    if not os.path.exists("photos"):
        os.makedirs("photos")

    for id, name in getfriends():
        url = "https://graph.facebook.com/" + id + "/picture"
        filename = os.path.join("photos", "%s.jpg" % (name))
        urlretrieve(url, filename)
        
def main():
    getphotos()
    
if __name__ == '__main__':
    main()
    
    