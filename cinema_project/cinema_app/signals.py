from django.db.models.signals import post_save
from django.dispatch import receiver
from cinema_app.models import Movie
from datetime import timedelta
from celery import shared_task


@receiver(post_save, sender=Movie)
def update_movie_ranking(sender, instance, created, **kwargs):
    if created and instance.status == 'coming_up':
        increase_ranking.apply_async(args=[instance.id], countdown=300)  # 300 seconds = 5 minutes


@shared_task
def increase_ranking(movie_id):
    movie = Movie.objects.get(id=movie_id)
    if movie.status == 'coming_up':
        movie.ranking += 10
        movie.save()
