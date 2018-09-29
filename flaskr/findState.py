import json
import urllib
from json import load
from urllib2 import urlopen

def getState():
        ip = load(urlopen('http://jsonip.com'))['ip']

        key = '80fc8c048d3d78bf47a861a5b4f4e6f1'
        api = 'http://api.ipstack.com/' + ip + '?access+key=' + key + '&format=1'
        result = urllib.urlopen(api).read()
        result = result.decode()
        result = json.loads(result)

        return result["region_name"]

getState()
