import urllib2
import json
from pprint import pprint


#Variable declarations
APIKey = "AIzaSyDIbJw0VKn8HpY0_eoj7rmbVwVZULAB9yU"
channelName = "MonstercatMedia"
channelFileName = "channel.json"
playlistFileName = "playlist.json"
playlistInfoFile = "Playlist Info.txt"
playlistCount = 0
playlistNames = []
playlistIDs = []

#Handles GET Request for finding channel ID
channelString = "https://www.googleapis.com/youtube/v3/channels?part=id&forUsername=" + channelName + "&key=" + APIKey

channelGrab = open(channelFileName, "w")
channelGrab.write(urllib2.urlopen(channelString).read())
channelGrab.close()

#Opens .json file to read in channel ID
with open(channelFileName) as channelDataFile:    
	channelData = json.load(channelDataFile)

channelID = channelData["items"][0]["id"]

channelDataFile.close()

#Prints for debugging
print("Number of items returned: %s" % (channelData["pageInfo"]["totalResults"]))
print("ChannelId: %s" % (channelID))


#Handles GET Request for finding playlist IDs and Names
playlistPageToken = ""
playlistString = "https://www.googleapis.com/youtube/v3/playlists?part=snippet&pageToken=" + playlistPageToken + "&channelId=" + channelID + "&key=" + APIKey

playlistGrab = open(playlistFileName, "w")
playlistGrab.write(urllib2.urlopen(playlistString).read())
playlistGrab.close()


with open(playlistFileName) as playlistDataFile:
	playlistData = json.load(playlistDataFile)

playlistDataFile.close()


playlistCount = playlistData["pageInfo"]["totalResults"]
playlistPageToken = playlistData["nextPageToken"]

print("Number of items returned: %s" % (playlistCount))

#Grab the name and IDs of all playlists
for i in range(0, playlistCount):

	for j in range(0, len(playlistData["items"])):
		playlistIDs.append(playlistData["items"][j]["id"])
		playlistNames.append(playlistData["items"][j]["snippet"]["title"])

	#Reassign url to be requested to change with page token
	try:
		playlistPageToken = playlistData["nextPageToken"]
	except KeyError:
		playlistPageToken = ""
	playlistString = "https://www.googleapis.com/youtube/v3/playlists?part=snippet&pageToken=" + playlistPageToken + "&channelId=" + channelID + "&key=" + APIKey
	playlistGrab = open(playlistFileName, "w")
	playlistGrab.write(urllib2.urlopen(playlistString).read())
	playlistGrab.close()

	with open(playlistFileName) as playlistDataFile:
		playlistData = json.load(playlistDataFile)

	playlistDataFile.close()


#Print playlist Names
for i in range(0, playlistCount):
	print(playlistNames[i])

#Print playlist IDs
for i in range(0, playlistCount):
	print(playlistIDs[i])

playlistWriter = open(playlistInfoFile, "w")
for i in range(0, playlistCount):
	InfoString = playlistNames[i] + ": " + playlistIDs[i] + "\n"
	playlistWriter.write(InfoString)


