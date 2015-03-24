from Media . import media 
import fresh_tomatoes


#Movies
class Movie(Video):
	def __init__(self, title, trailer_youtube):
		Video.__init__(self, title, trailer_youtube)
		self.runtime = self.dat['runtimes'][0]

	def show_info(self):
		return ("<p><strong>Title: </strong>" + str(self.title) +"</p>"
				"<p><strong>Storyline: </strong>" + str(self.storyline) + "</p>"
				"<p><strong>Runtime: </strong>" + str(self.runtime) + "</p>")

#TV Shows
class TvShow(Video):

	"""This class provides a way to store TV-related information and display its information"""

	def __init__(self, title, trailer):
		Video.__init__(self, title, trailer)
		self.season = show.dat['seasons']
		self.runtime = show.dat['runtimes'][0]

	def show_info(self):
		return ("<p><strong>Title: </strong>" + str(self.title) + "</p>"
                "<p><strong>Storyline: </strong>" + str(self.storyline) + "</p>"
                "<p><strong>Seasons: </strong>" + str(self.seasons) + "</p>"
                "<p><strong>Runtime: </strong>" + str(self.runtime) + "</p>")

#print(media.Movie.VALID_RATINGS)

toy_story = Movie("Toy Story", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

goodfellas = media.Movie("Goodfellas", "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

hunger_games = media.Movie("Hunger Games", "https://www.youtube.com/watch?v=mfmrPu43DF8")

ratatouille = media.Movie("Ratatouille", "https://www.youtube.com/watch?v=niD-jahFURU")

the_office = media.TvShow("The Office", "http://theoffice.so/0645.html")

movies = {"name": "Movies", 
			"content":[toy_story, avatar, school_of_rock, goodfellas, hunger_games, ratatouille]}

tv_shows = {"name": "TV Shows",
			"content": [the_office]}

cont = [movies, tv_shows]

fresh_tomatoes.open_movies_page(cont)





