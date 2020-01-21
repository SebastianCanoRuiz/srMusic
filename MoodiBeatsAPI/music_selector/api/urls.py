# api/urls.py
from django.conf.urls import url
from .views import *

urlpatterns = [
 url(r'^new-videos/$', NewVideoAPIView.as_view()),
 url(r'^songs-moods/(?P<mood>\d{1})/$', getMoodData),
 url(r'^songs-genres-moods/(?P<mood>\d{1})/(?P<genre>\w+)/$', getMoodGenreData),
]