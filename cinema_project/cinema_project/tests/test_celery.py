# from cinema_app.signals import update_movie_ranking
# from cinema_app.models import Movie
# from django.utils import timezone
# import pytest
# from celery import Task
#
#
# class CeleryTaskMock(Task):
#     def apply_async(self, args=None, kwargs=None, **options):
#         self.run(*args, **kwargs)
#
#
# @pytest.fixture
# def celery_task_mock(monkeypatch):
#     monkeypatch.setattr("cinema_app.tasks.update_movie_ranking", CeleryTaskMock())
#
#
# def test_update_movie_ranking(celery_task_mock):
#     movie = Movie.objects.create(name="Test Movie", protagonists="John Doe", poster="poster.jpg", trailer="trailer.mp4",
#                                  start_date=timezone.now(), status="coming_up", ranking=0)
#     update_movie_ranking()
#     movie.refresh_from_db()
#     assert movie.ranking == 10
