from pyechonest import config
config.ECHO_NEST_API_KEY = "ZQXJHQWPS4UO54AUV"

from pyechonest import artist
bk = artist.Artist('Kailesh Kher');
print "Artists similar to %s:" %(bk.name)
for similar_artist in bk.similar:
	print "\t%s" % (similar_artist.name)
