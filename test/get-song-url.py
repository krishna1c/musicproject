from pyechonest import config
config.ECHO_NEST_API_KEY = "ZQXJHQWPS4UO54AUV"

from pyechonest import song
ss = song.search(artist='the national',title = 'slow show', buckets=['id:7digital-US','tracks'], limit = True)
slow_show = ss[0]
ss_trackes = slow_show.get_tracks('7digital-US')
print ss_trackes[0].get('analysis_url')
