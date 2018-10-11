import requests

# Part 3 - Server Side Requests
#
# Using the requests module and the OMDB API, build an application that
# prompts the user for two pieces of information, the name of an
# actor/actress and a movie. Your program should tell the user if that
# actor or actress was in that movie (this will only work for leading
# actors and actresses). As a bonus, add functionality to tell users
# who the director and writer of a movie were.


def more_info(movie, movie_request):
    info = input(f"Would you like more information about {movie}? Y/N: ")
    if info.strip()[0].upper() == 'Y':
        director, writer = movie_request['Director'], movie_request['Writer']
        return f"\n{movie} was directed by {director} and written by {writer}"
    else:
        return "\nBye!"


def check_actors(actor, movie, movie_request):
    actors = map(lambda n: n.strip(), movie_request['Actors'].split(','))
    if actor in actors:
        return f"\nYes, {actor} was in {movie}"
    else:
        return f"\nNo, {actor} was not in {movie}"


if __name__ == "__main__":
    print("Welcome to movie search, let's check if an actor or actress was in a movie")
    actor = input("Actor/Actress: ").strip().title()
    movie = input("Movie: ").strip().title()

    api = f"http://www.omdbapi.com?apikey=f80c4327&t={movie}"
    movie_request = requests.get(api).json()

    if movie_request['Response'] == 'True':
        print(check_actors(actor, movie, movie_request))
        print(more_info(movie, movie_request))
    else:
        print(f"\n{movie} was not found in the movie database")
        