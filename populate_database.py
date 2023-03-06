import csv
import os
from repository import Repository
from models import Movie

movie_repository = Repository()

def start():
    all_files = os.listdir('.')
    for filename in all_files:
        if filename.endswith('.csv'):
            data = get_data(filename=filename)

def get_data(filename=None):
    default_fields = ['year', 'title', 'studios', 'producers', 'winner']
    if filename:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f, fieldnames=default_fields, delimiter=';')
            next(reader)
            for data in reader:
                insert_to_db(data)

def insert_to_db(data):
    data = dict(data)
    movie = movie_repository.get_by_field(Movie, Movie.title, data.get('title', None))
    if not movie.first():
        from datetime import datetime
        mv = Movie(
            year = data.get('year', None),
            title = data.get('title', None),
            studios = data.get('studios', None),
            producers = data.get('producers', None),
            winner = bool(data.get('winner', None))
        )
        movie_repository.add(mv)

def create_table():
    movie_repository.create_table(Movie)

if __name__ == '__main__':
    create_table()
    start()