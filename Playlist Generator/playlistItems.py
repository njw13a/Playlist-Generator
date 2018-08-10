import urllib2
import re
import json
from pprint import pprint

APIKey = "AIzaSyDIbJw0VKn8HpY0_eoj7rmbVwVZULAB9yU"
channelName = "MonstercatMedia"
channelFileName = "channel.json"
playlistFileName = "playlist.json"
playlistItemsFileName = "playlistItems.json"
playlistInfoFile = "Playlist Info.txt"
songListFile = "Song List"
playlistCount = 0
songNames = []
songIDs = []

playlistItemsFileName
playlistID = "PLe8jmEHFkvsYv5CV7wSLZk7UG41KY8q_Q"

playlistItemsString = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=" + playlistID + "&key=" + APIKey

playlistItemGrab = open(playlistItemsFileName, "w")
playlistItemGrab.write(urllib2.urlopen(playlistItemsString).read())
playlistItemGrab.close()


with open(playlistItemsFileName) as playlistItemsDataFile:
	playlistItemsData = json.load(playlistItemsDataFile)

playlistItemsDataFile.close()


playlistItemsCount = playlistItemsData["pageInfo"]["totalResults"]
playlistItemsPageToken = playlistItemsData["nextPageToken"]

print("Number of items returned: %s" % (playlistItemsCount))

#Grab the name and IDs of all playlists
for i in range(0, playlistItemsCount):

	for j in range(0, len(playlistItemsData["items"])):
		songIDs.append(playlistItemsData["items"][j]["snippet"]["resourceId"]["videoId"])
		songNames.append(re.sub("[\[].*?[\]]", "", playlistItemsData["items"][j]["snippet"]["title"]))
	
	#Reassign url to be requested to change with page token
	try:
		playlistItemsPageToken = playlistItemsData["nextPageToken"]
	except KeyError:
		playlistItemsPageToken = ""
	playlistItemsString = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&pageToken=" + playlistItemsPageToken + "&playlistId=" + playlistID + "&key=" + APIKey
	playlistItemsGrab = open(playlistItemsFileName, "w")
	playlistItemsGrab.write(urllib2.urlopen(playlistItemsString).read())
	playlistItemsGrab.close()

	with open(playlistItemsFileName) as playlistItemsDataFile:
		playlistItemsData = json.load(playlistItemsDataFile)

	playlistItemsDataFile.close()

#regex = re.compile(".*?\[.*?].*?\[.*?]")
#result = re.findall(regex, songNames[15])


playlistItemsWriter = open(songListFile, "w")
for i in range(0, playlistItemsCount):
	InfoString = songNames[i] + ": " + songIDs[i] + "\n"
	playlistItemsWriter.write(InfoString)