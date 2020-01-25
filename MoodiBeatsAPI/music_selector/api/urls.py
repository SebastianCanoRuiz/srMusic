# api/urls.py
from django.conf.urls import url
from .views import NewVideoAPIView, getMoodData, getGenreData, getGenreMoodData, getNameData, getNameMoodData, getNameGenreData, getNameMoodGenreData

urlpatterns = [
 url(r'^new-videos/$', NewVideoAPIView.as_view()),
 url(r'^songs-mood/(?P<mood>[^/]+)/$', getMoodData),
 url(r'^songs-genre/(?P<genre>[^/]+)/$', getGenreData),
 url(r'^songs-genre-mood/(?P<genre>[^/]+)/(?P<mood>[^/]+)/$', getGenreMoodData),
 url(r'^songs-name/(?P<name>[^/]+)/$', getNameData),
 url(r'^songs-name-mood/(?P<name>[^/]+)/(?P<mood>[^/]+)/$', getNameMoodData),
 url(r'^songs-name-genre/(?P<name>[^/]+)/(?P<genre>[^/]+)/$', getNameGenreData),
 url(r'^songs-name-mood-genre/(?P<name>[^/]+)/(?P<mood>[^/]+)/(?P<genre>[^/]+)$', getNameMoodGenreData),
]