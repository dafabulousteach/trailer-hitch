import webbrowser
import imdb
import fresh_tomatoes

def get_info(title):
		i = imdb.IMDb()
		lst = i.search_movie(title)
		match = lst[0]
		i.update(match)
		return match

class Video():
	def __init__(self, title, trailer):
		self.title = title
		self.dat = get_info(title)
		self.storyline = self.dat['plot outline']
		self.poster = self.dat['full-size cover url']
		self.genre = self.dat['genre'][0]
		self.trailer = trailer
