from movie import Movie
from rating_system import RatingSystem

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