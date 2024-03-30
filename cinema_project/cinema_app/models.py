from django.db import models


class Movie(models.Model):
    STATUS_CHOICES = (
        ('coming_up', 'Coming Up'),
        ('starting', 'Starting'),
        ('running', 'Running'),
        ('finished', 'Finished')
    )
    name = models.CharField(max_length=100)
    protagonists = models.CharField(max_length=500)
    poster = models.ImageField(upload_to='posters/')
    trailer = models.FileField(upload_to='trailers/')
    start_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='coming_up')
    ranking = models.IntegerField(default=0)
    last_ranking_update = models.DateTimeField(auto_now_add=True)

