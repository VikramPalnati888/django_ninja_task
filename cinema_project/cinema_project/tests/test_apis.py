import tempfile

import pytest
import requests
from django.urls import reverse
from rest_framework import status
from PIL import Image

url = 'http://127.0.0.1:8000'


def temporary_image():
    image = Image.new('RGB', (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg', prefix="test_img_")
    image.save(tmp_file, 'jpeg')
    tmp_file.seek(0)
    return tmp_file


@pytest.mark.db
def test_movies_get():
    payload = {
        "name": "testing",
        "protagonists": "string",
        "poster": "/string.jpg",
        "trailer": "/string1.mp4",
        "start_date": "2027-09-09",
        "status": "coming_up",
        "ranking": 9
    }
    response = requests.post(url + "/api/movies", json=payload)
    assert response.status_code == 200



@pytest.mark.db
def test_movies():
    response = requests.get(url + "/api/movies")
    response.json()
    print(response.json(),"aaaaaaaaaaaaaaaaaaaaaaaa")
    assert response.status_code == 200
