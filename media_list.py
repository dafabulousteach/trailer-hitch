import parent_class
import fresh_tomatoes

toy_story = parent_class.Movie("Toy Story", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = parent_class.Movie("Avatar", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

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