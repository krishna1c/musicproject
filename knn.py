import csv
import random
import sys
import math
from math import sqrt
from operator import itemgetter
energyArray = {1:1,2:0.5,3:0}
danceabilityArray = {1:1,2:0}
valenceArray = {1:1,2:0,3:0.5}
livenessArray = {1:0.9,2:0.7,3:0.3}
speechinessArray = {1:1,2:0.5,3:0}
loudnessArray = {1:0,2:-15,3:-30,4:-45,5:-60}
acousticnessArray = {1:1,2:0}
def loadDataSet():
	songsData = []
	with open('songlist.dat','r') as songFile:
		reader = csv.reader(songFile, delimiter = "\t")
		songsList = list(reader)
		for x in range(len(songsList)-1):	
			songsData.append({});
			songsData[x]['title'] = songsList[x][3]
			songsData[x]['energy'] = float(songsList[x][9])
			songsData[x]['liveness'] = float(songsList[x][10])
			songsData[x]['speechiness'] = float(songsList[x][12])
			songsData[x]['acousticness'] = float(songsList[x][13])
			songsData[x]['danceability'] = float(songsList[x][14])
			songsData[x]['loudness'] = float(songsList[x][18])
			songsData[x]['valence'] = float(songsList[x][19])
	return songsData

def takeInput():
	print "Please describe the song you want to hear"
	energyInput = raw_input("What is the energy level?\n1: High Energy, 2: Moderate energy, 3: Not so energetic\n")
	livenessInput = raw_input("What is the liveness?\n1: Live, 2: Partially live, 3: Studio recording\n")
	speechinessInput = raw_input("What is the speechiness?\n1: Spoken song, 2: Both speech and music, 3: Mostly music\n")
	acousticnessInput = raw_input("What is the acousticness of the song?\n1: High, 2: Low\n")
	danceabilityInput = raw_input("What is the danceability of the song?\n1: Danceable, 2: Not so danceable\n")
	loudnessInput = raw_input("How loud is the song?\n1: Extremely loud, 2: Loud, 3: Moderate, 4: Soft, 5: Very soft\n")
	valenceInput = raw_input("What is the mood of the song?\n1: Happy, 2: Sad, 3: Neutral\n")
	energy = energyArray[int(energyInput)]
	liveness = livenessArray[int(livenessInput)]
	speechiness = speechinessArray[int(speechinessInput)]
	acousticness = acousticnessArray[int(acousticnessInput)]
	danceability = danceabilityArray[int(danceabilityInput)]
	loudness = loudnessArray[int(loudnessInput)]
	valence = valenceArray[int(valenceInput)]
	mySong = {}
	mySong['energy'] = energy
	mySong['liveness'] = liveness
	mySong['speechiness'] = speechiness
	mySong['acousticness'] = acousticness
	mySong['danceability'] = danceability
	mySong['loudness'] = loudness
	mySong['valence'] = valence
	return mySong

def euclideanDistance(song1, song2):
	dist = 0.0
	for key, value in song1.iteritems():
		if key != 'title' and key!='loudness':
			dist += pow(song1[key]-song2[key],2)
		if key == 'loudness':
			dist += pow((song1[key]-song2[key])/60,2)
	return sqrt(dist)

def getTop10Recommendations(preferences, songsData):
	preferences['title'] = 'To be found'
	ordering = []
	for x in range(len(songsData)-1):
		ordering.append({})
		ordering[x]['title'] = songsData[x]['title']
		ordering[x]['euclideanDistance'] = euclideanDistance(songsData[x],preferences)

	sortedOrdering = sorted(ordering, key = itemgetter('euclideanDistance'))
	sortedOrdering = [dict(t) for t in set([tuple(d.items()) for d in sortedOrdering])]
	return sortedOrdering[1:101]

if __name__ == '__main__':
    mySong = takeInput()
    songsData = loadDataSet()
    top100 = getTop10Recommendations(mySong,songsData)
    for song in top100:
    	print song['title']#, song['euclideanDistance']

