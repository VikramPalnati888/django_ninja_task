import json

from ninja import NinjaAPI, Schema, ModelSchema
from django.shortcuts import get_object_or_404
from cinema_app.models import Movie
from django.forms.models import model_to_dict

api = NinjaAPI()
url = 'http://127.0.0.1:8000'

class MovieGetSchema(ModelSchema):
    class Meta:
        model = Movie
        fields = "__all__"


class MoviePostSchema(Schema):
    name: str
    protagonists: str
    poster: str
    trailer: str
    start_date: str
    status: str
    ranking: int


@api.get("/movies/{movie_id}", response=MovieGetSchema)
def movie_details(request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    return movie


@api.get("/movies", response=list[MovieGetSchema])
def movies_list(request):
    return Movie.objects.all().order_by('-ranking')


@api.post("/movies")
def movies_create(request, payload: MoviePostSchema):
    response_data = {}
    obj = Movie.objects.create(**payload.dict())
    movies_data = model_to_dict(obj)
    movies_data['poster'] = url+'/cinema_project/media'+str(movies_data['poster'])
    movies_data['trailer'] = url + '/cinema_project/media' + str(movies_data['trailer'])
    return movies_data
