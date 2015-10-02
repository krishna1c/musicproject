from pyechonest import config
config.ECHO_NEST_API_KEY = "ZQXJHQWPS4UO54AUV"

from pyechonest import artist
a = artist.Artist("musicbrainz:artist:a74b1b7f-71a5-4011-9441-d0b5e4122711")
print a.name
