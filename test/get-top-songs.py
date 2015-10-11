import os
import sys
import time
from pyechonest import config
config.ECHO_NEST_API_KEY = "ZQXJHQWPS4UO54AUV"

from pyechonest import song
count = 0
fin = open('unique_tracks.txt','r')
fout = open('songlist.dat','a+')
for line in fin:
	splits = line.split("<SEP>")
	title = splits[2]	
	results = song.search(title = title, buckets = ['audio_summary','song_currency', 'song_discovery', 'song_hotttnesss', 'song_type'], results = 1)
	if(len(results) == 0):
		count = count + 1
		if(count%20 == 0):
			time.sleep(60)
		continue
	s = results[0]
	l = []
	l.append(unicode(s.artist_id))
	l.append(unicode(s.artist_name))
	l.append(unicode(s.id))
	l.append(unicode(s.title))
	l.append(unicode(s.song_currency))
	l.append(unicode(s.song_discovery))
	l.append(unicode(s.song_hotttnesss))
	l.append(unicode(s.song_type))
	l.append(unicode(s.audio_summary['time_signature']))
	l.append(unicode(s.audio_summary['energy']))
	l.append(unicode(s.audio_summary['liveness']))
	l.append(unicode(s.audio_summary['tempo']))
	l.append(unicode(s.audio_summary['speechiness']))
	l.append(unicode(s.audio_summary['acousticness']))
	l.append(unicode(s.audio_summary['danceability']))
	l.append(unicode(s.audio_summary['instrumentalness']))
	l.append(unicode(s.audio_summary['key']))
	l.append(unicode(s.audio_summary['duration']))
	l.append(unicode(s.audio_summary['loudness']))
	l.append(unicode(s.audio_summary['valence']))
	fout.write('\t'.join(l).encode('utf-8'))
	fout.write('\n')
	count = count + 1
	print 'Wrote record %d' % (count)
	if (count % 20 == 0):
		time.sleep(60)
fin.close()
fout.close()
