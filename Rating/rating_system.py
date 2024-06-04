from movie import Movie

class RatingSystem:
    #Create movies list for rating
    def __init__(self):
        self.movies = []

    #Add movie to the rating movies list
    def addMovie(self, movie):
        self.movies.append(movie)

    #Rating the movie
    def rateMovie(self, title, rating):
        for movie in self.movies:
            if movie.title == title:
                movie.rate(rating)
                return
        print("Movie not found.")
    
    #Average Rating
    def getAverage(self):
        totalRating = 0
        totalMovie = 0
        for movie in self.movies:
            if movie.rating is not None:
                totalRating = totalRating + movie.rating
                totalMovie = totalMovie + 1
            else:
                return "No movies rated" #Returns 0 if no movies are rated
        return totalRating / totalMovie
    
    def viewRatings(self):
        for movie in self.movies:
            #Views ratings for each movie and returns not rated if none
            if movie.rating is not None:
                print("{} - Rated: {}".format(movie.title, movie.rating))
            else:
                print("{} - Not rated yet".format(movie.title))

    def groupGenre(self):
        genres = {}
        #Could add way to group by genres and return that
        for movie in self.movies:
            if movie.genre in genres:
               genres[movie.genre].append(movie)
            else:
                genres[movie.genre] = [movie]
        return genres