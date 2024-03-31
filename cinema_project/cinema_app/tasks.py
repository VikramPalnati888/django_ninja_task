from celery import shared_task
from .models import Movie
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movie


@receiver(post_save, sender=Movie)
def update_movie_status(sender, instance, created, **kwargs):
    if created and instance.status == 'running':
        update_movie_ranking.delay()

@shared_task
def update_movie_ranking():
    movies = Movie.objects.filter(status='coming_up')
    for movie in movies:
        movie.ranking += 10
        movie.save()
