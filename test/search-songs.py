from pyechonest import config
config.ECHO_NEST_API_KEY = "ZQXJHQWPS4UO54AUV"

from pyechonest import song
rkp_results = song.search(artist = 'radiohead', title='karma police')
kp = rkp_results[0]
print kp.artist_location
print 'Temp:', kp.audio_summary['tempo'],'duration:',kp.audio_summary['duration']
