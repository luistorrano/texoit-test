from flask import *
from repository import Repository
from sqlalchemy import func
import services
from models import Movie
import json

app = Flask(__name__)
movie_repository = Repository()

'''
Considerações:
Os requisitos da API aparentemente estão incoerentes com o resultado esperado,
pois no resultado é mencionado mais de um producer, enquanto no requisito é mencionado apenas um producer. Isto influencia também no previousWin,
o qual foi necessário considerar o primeiro ano no qual o producer venceu o prêmio.
Existem também produções em conjunto, no qual existe um produtor que produziu mais filmes da lista, porém sozinho ou com outros produtores.
Desta forma, considerei as produções de filmes realizadas pelo(s) mesmo(s) produtor(es), e também considerei apenas o que foi pedido no requisito (um producer) 
'''

@app.route('/interval', methods=['GET'])
def getInterval():
    if request.method == 'GET':
        winner_producers = movie_repository\
            .get_by_field(Movie.producers, Movie.winner, True)\
            .group_by(Movie.producers)\
            .having(func.count(Movie.producers) > 1)\
            .all()
        max_interval = services.get_max(winner_producers)
        min_interval = services.get_min(winner_producers)
        return json.dumps(dict(
            min = min_interval,
            max = max_interval
        ))

if __name__ == '__main__':
    app.run(port=8888)