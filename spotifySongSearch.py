import urllib2
import json
from pprint import pprint

songGrabFileName = "Song Grab"

url = "https://api.spotify.com/v1/search?q=Stephen+Walking+-+Claptrap&type=track"

req = urllib2.Request(url)
req.add_header('Accept', 'application/json')
req.add_header('Authorization', 'Bearer BQBcoYPHwDwiWk75YByP13_RXsppy2E0J7SsLvGJgCZv461uc7yTo9dN77A3NHmdN3hQRoU5hn4AJ37VWi5WH8_KXV69qsPUgCmnx4WRU3froihE_XU8TatRBbT5ynVp8uMWWYQTfkpIm1yFXxAildObrtF2cBO3AAWVdapSVbFlGEAUwA1ej9uPSJdVH7KBFp2VAASUvgjR-fpVzRXUmB29kbIDdelqWvpFCqaW')

songGrab = open(songGrabFileName, "w")
songGrab.write(urllib2.urlopen(req).read())
songGrab.close()

with open(songGrabFileName) as songGrabDataFile:
	songGrabData = json.load(songGrabDataFile)


print(songGrabData["tracks"]["items"][0]["uri"])
#songGrab = open(songGrabFile, "w")
#songGrab.write(req.read())





'''playlistItemGrab = open(playlistItemsFileName, "w")
playlistItemGrab.write(urllib2.urlopen(playlistItemsString).read())
playlistItemGrab.close()


with open(playlistItemsFileName) as playlistItemsDataFile:
	playlistItemsData = json.load(playlistItemsDataFile)

playlistItemsDataFile.close()'''