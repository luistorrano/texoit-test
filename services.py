from repository import Repository
from models import Movie

movie_repository = Repository()

def get_min_diff(producers_list):
    differences = []
    for p in producers_list:
        movies = movie_repository.get_by_field(Movie, Movie.producers, p).order_by(Movie.year.asc()).all()
        fm = movies[0].year
        lm = movies[-1].year
        difference = lm - fm
        differences.append({'difference': difference, 'producer': movies[0].producers})
    minimum_difference = min(differences, key=lambda x:x.get('difference'))
    return minimum_difference

def get_max_diff(producers_list):
    differences = []
    for p in producers_list:
        movies = movie_repository.get_by_field(Movie, Movie.producers, p).order_by(Movie.year.asc()).all()
        fm = movies[0].year
        lm = movies[-1].year
        difference = lm - fm
        differences.append({'difference': difference, 'producer': movies[0].producers})
    maximum_difference = max(differences, key=lambda x:x.get('difference'))
    return maximum_difference

def transform_list(tuple_list):
    l = []
    for tl in tuple_list:
        l.append(tl[0])
    return l

def get_min(producers_list):
    producers = transform_list(producers_list)
    minimum_difference = get_min_diff(producers)
    min_dif = movie_repository.get_by_field(Movie, Movie.producers, minimum_difference.get('producer'))\
    .order_by(Movie.year.asc()).all()

    return [
            dict(
                producer = minimum_difference.get('producer'),
                interval = min_dif[-1].year - min_dif[0].year,
                previousWin = min_dif[0].year,
                followingWin = min_dif[1].year
            )
       ]
def get_max(producers_list):
    producers = transform_list(producers_list)
    maximum_difference = get_max_diff(producers)
    max_dif = movie_repository.get_by_field(Movie, Movie.producers, maximum_difference.get('producer'))\
    .order_by(Movie.year.asc()).all()
    return [
            dict(
                producer = maximum_difference.get('producer'),
                interval = max_dif[-1].year - max_dif[0].year,
                previousWin = max_dif[0].year,
                followingWin = max_dif[1].year
            )
        ]