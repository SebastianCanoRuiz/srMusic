# api/urls.py
from django.conf.urls import url
from .views import NewVideoAPIView, getMoodData, getMoodGenreData, getNameData

urlpatterns = [
 url(r'^new-videos/$', NewVideoAPIView.as_view()),
 url(r'^songs-mood/(?P<mood>[^/]+)/$', getMoodData),
 url(r'^songs-mood-genre/(?P<mood>[^/]+)/(?P<genre>[^/]+)/$', getMoodGenreData),
 url(r'^songs-name/(?P<name>[^/]+)/$', getNameData),
]