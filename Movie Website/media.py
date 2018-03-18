import webbrowser

class Video():
    def __init__(self, title,duration):
        self.title=title
        self.duration=duration


class Movie(Video):
    """This class provide a way to store movie related information"""
    VALID_RATINGS=["G","PG","PG-13","R"]
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open_new(self.trailer_youtube_url)






class TVShow(Video):
    def __init__(self, show_title, show_season,
                 show_episode,show_tv_station):
        self.title=show_title
        self.season=show_season
        self.episode=show_episode
        self.station=show_tv_station
    def get_local_listing(self):
        pass

#https://google.github.io/styleguide/pyguide.html
#https://docs.python.org/2.7/tutorial/classes.html#random-remarks
#https://discussions.udacity.com/t/play-movie-trailer-f/16114/7141
#https://discussions.udacity.com/c/standalone-courses/programming-foundations-with-python
#https://docs.python.org/2/tutorial/introduction.html#lists
#https://www.wired.com/2011/08/python-notes-lists-vs-arrays/
#http://www2.lib.uchicago.edu/keith/courses/python/class/5/