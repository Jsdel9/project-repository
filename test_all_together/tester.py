
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

#Example Movies
movie1 = Movie("Good Will Hunting", "Drama")
movie2 = Movie("Princess Bride", "Comedy")
movie3 = Movie("Shrek", "Comedy")
movie4 = Movie("What's Eating Gilbert Grape", "Drama")
movie5 = Movie("The Shawshank Redemption", "Drama")
movie6 = Movie("The Wolf of Wall Street", "Comedy")
movie7 = Movie("The Peanut Butter Falcon", "Comedy")
movie8 = Movie("La La Land", "Drama")
movie9 = Movie("Remember the Titans", "Drama")
movie10 = Movie("Ocean's Eleven", "Comedy")

#Example adding movies to rating system
ratingsystem = RatingSystem()
ratingsystem.addMovie(movie1)
ratingsystem.addMovie(movie2)
ratingsystem.addMovie(movie3)
ratingsystem.addMovie(movie4)
ratingsystem.addMovie(movie5)
ratingsystem.addMovie(movie6)
ratingsystem.addMovie(movie7)
ratingsystem.addMovie(movie8)
ratingsystem.addMovie(movie9)
ratingsystem.addMovie(movie10)

#Example adding ratings to rating system
ratingsystem.rateMovie("Good Will Hunting", 10)
ratingsystem.rateMovie("Princess Bride", 10)
ratingsystem.rateMovie("Shrek", 6)
ratingsystem.rateMovie("What's Eating Gilbert Grape", 8.5)
ratingsystem.rateMovie("The Shawshank Redemption", 9)
ratingsystem.rateMovie("The Wolf of Wall Street", 8.5)
ratingsystem.rateMovie("The Peanut Butter Falcon", 8)
ratingsystem.rateMovie("La La Land", 8)
ratingsystem.rateMovie("Remember the Titans", 10)
ratingsystem.rateMovie("Ocean's Eleven", 9)

#See all ratings
print("All Ratings:")
ratingsystem.viewRatings()

#See average for all movies in list
print(f"Average Rating is: {ratingsystem.getAverage()}")

#Final print sorted by genres

print("\nSorted by Genre:")
genres = ratingsystem.groupGenre()
for genre, movies in genres.items():
    print("\n{} Movies:".format(genre))
    for movie in movies:
        print("{} - Rating: {}".format(movie.title, movie.rating))