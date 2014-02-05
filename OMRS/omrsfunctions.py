__author__ = 'judyw'

import requests,json,re
from requests.auth import HTTPBasicAuth

#variables
url = str('http://localhost:8081/openmrs-standalone/ws/rest/v1/')
url2 = str('http://162.222.179.9:8080/kenyacaptricity/ws/rest/v1/')
headers = {'content-type': 'application/json'}
username = 'admin'
pw = 'test'

def searchLocations(server,username,password):
    #server = str(server)+ '/ws/rest/v1/'
    p = requests.get(server+'location',headers=headers,auth=HTTPBasicAuth(username,password))
    resp = json.loads(p.text)
    locations = resp['results']  #list of locations returned

    locationdict ={} # holds all searched locations as key/value pairs

    #get the location uuid and name
    for k,v in enumerate(locations):
        locationUUID = locations[k]['uuid']
        locationName = locations[k]['display']
        locationdict[locationUUID] = locationName
    #print type(locationdict)
    print locationdict
    return locationdict


#searchLocations(url,'admin','test')

def searchEncounterTypes():
    return 'yaya'

def searchIdentifiers():
    return 'more yaya'