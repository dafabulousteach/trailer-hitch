import webbrowser
import imdb

imdb_access = imdb.IMDb()
class Video():
	"""This class provides a way to store movie related information and display its information"""

	def getinfo(title):
		i = imdb.IMDb()
		lst = i.search_movie(title)
		match = lst[0]
		i.update(match)
		return match
		
	def __init__(self, title, trailer):
		self.title = title
		self.dat = getinfo(title)
		self.storyline = self.dat['plot outline']
		self.poster = self.dat['full-size cover url']
		self.trailer = trailer.url

	
		
	#def show_trailer(self):
		#webbrowser.open(self.trailer_youtube_url)