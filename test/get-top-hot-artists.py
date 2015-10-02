from pyechonest import config
config.ECHO_NEST_API_KEY = "ZQXJHQWPS4UO54AUV"

from pyechonest import artist
for hot_artist in artist.top_hottt():
	print hot_artist.name, hot_artist.hotttnesss
