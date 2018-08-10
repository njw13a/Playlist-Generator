import urllib2
import json
from pprint import pprint

songGrabFileName = "Song Grab"

songRequest =  "Stephen+Walking+-+Claptrap"
url = "https://api.spotify.com/v1/search?q=" + songRequest + "&type=track"
token = "Bearer BQCRf_Oesqc-oYidm3553Zsyp0mSNcoTOT1lNw-GNVg_uETOoaMMsyX5xMY3thPbJBlX5KED-72ycK38Yk-SVN4Qt0LXbSNrT_NuGg0hr1Tsn5sSa-AXpfp-DOQe1puUNuCLGAZZwcpamt4dFi7Rl1uzexx8KfG3ZuTCwUuuzP6NKx3ytDE6BQ0d5yO2Jsm6X2voG5B33vEYJhaNR1SpXLLe9F_-ULAyYNs1Ebcp"


req = urllib2.Request(url)
req.add_header('Accept', 'application/json')
req.add_header('Authorization', token)

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