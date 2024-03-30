from ninja import NinjaAPI, Schema, ModelSchema
from django.shortcuts import get_object_or_404
from cinema_app.models import Movie

api = NinjaAPI()


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


@api.get("/movie/{movie_id}", response=MovieGetSchema)
def movie_details(request, movie_id:int):
    movie = get_object_or_404(Movie, id=movie_id)
    return movie


@api.get("/movies", response=list[MovieGetSchema])
def movies_list(request):
    return Movie.objects.all().order_by('-ranking')


@api.post("/movies", response=MovieGetSchema)
def movies_create(request, payload: MoviePostSchema):
    movie_obj = Movie.objects.create(**payload.dict())
    return movie_obj
