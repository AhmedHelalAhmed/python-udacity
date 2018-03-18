import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print toy_story.storyline



avatar = media.Movie("Avatar",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print (avatar.storyline)
#avatar.show_trailer()
flubber = media.Movie("Flubber",
                        "An absent-minded professor discovers flubber, a rubber-like super-bouncy substance.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/82/Flubber.jpg/220px-Flubber.jpg",
                        "https://www.youtube.com/watch?v=74whfeXZTrg")
#flubber.show_trailer()

movies=[toy_story, avatar, flubber]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__) #to get the documentation of my class
#print(media.Movie.__name__)
#print(media.Movie.__module__)



#https://discussions.udacity.com/t/play-movie-trailer-f/16114/7141
#https://discussions.udacity.com/c/standalone-courses/programming-foundations-with-python
#http://www2.lib.uchicago.edu/keith/courses/python/class/5/

