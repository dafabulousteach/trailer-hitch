import fresh_tomatoes
import media

class TvShow(Video):

	"""This class provides a way to store TV-related information and display its information"""

	def __init__(self, title, trailer):
		Video.__init__(self, title, trailer)
		self.season = show.dat['seasons']
		self.runtime = show.dat['runtimes'][0]

	return ("<p><strong>Title: </strong>" + str(self.title) + "</p>"
                "<p><strong>Storyline: </strong>" + str(self.storyline) + "</p>"
                "<p><strong>Seasons: </strong>" + str(self.seasons) + "</p>"
                "<p><strong>Runtime: </strong>" + str(self.runtime) + "</p>")