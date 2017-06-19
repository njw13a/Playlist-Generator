import urllib2
import json
from pprint import pprint

clientID = "c62a0185230f47ac827410cb8e9b9c18"
redirectURI = "https://www.google.com/"

url = "https://accounts.spotify.com/authorize?client_id=" + clientID + "&response_type=code" #&redirect_uri=" + redirectURI

urlReturn = urllib2.urlopen(url).read()

print(urlReturn)