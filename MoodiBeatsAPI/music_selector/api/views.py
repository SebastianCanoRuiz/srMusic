from rest_framework.response import Response
from rest_framework import generics
from songs.models import NewVideo
from .serializers import NewVideoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.http import JsonResponse

# Create your views here.


class NewVideoAPIView(generics.ListCreateAPIView):
    queryset = NewVideo.objects.all()
    serializer_class = NewVideoSerializer

def switch(argument):
    switcher = {1: 'HAPPY', 2: 'IN-LOVE', 3: 'SAD', 4: 'ANGRY'}
    return switcher.get(int(argument))

def getMoodData(*args, **kwargs):
    numberMood = switch(kwargs.get('mood'))
    queryset = NewVideo.objects.filter(moods=numberMood)
    data = list(queryset.values("video_id", "video_title"))
    return JsonResponse(data, safe=False)
