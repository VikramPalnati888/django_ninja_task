import pytest
import requests
from django.urls import reverse
from rest_framework import  status


@pytest.mark.django_db
def test_movies_get():
    url = reverse('/movies')
    data = {
        "name": "Test Movie 2222",
        "protagonists": "John Doe",
        "poster": "/test_poster.jpg",
        "trailer": "/test_trailer.mp4",
        "start_date": "2024-03-30",
        "status": "coming_up",
        "ranking": 4,
    }
    response = requests.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
