from pyechonest import config
config.ECHO_NEST_API_KEY = "ZQXJHQWPS4UO54AUV"

from pyechonest import artist
anu_result = artist.search(name = 'Anu Malik')
anu = anu_result[0]
anu_blogs = anu.blogs
print 'Blogs about anu:', [blog.get('url') for blog in anu_blogs]
