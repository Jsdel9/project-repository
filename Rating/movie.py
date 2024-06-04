from rating_system import RatingSystem

class Movie:
    #Say what movie using title
    def __init__ (self, title, genre):
        self.title = title
        self.genre = genre
        self.rating = None #Creates the object for later calling

    #Creates rating
    def rate(self, rating):
        if 0 <= rating <= 10:
            self.rating = rating
        else:
            print("Rating should be between 0 and 10.")
    