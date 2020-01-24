from rest_framework.response import Response
from rest_framework import generics
from songs.models import NewVideo
from .serializers import NewVideoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.http import JsonResponse

class NewVideoAPIView(generics.ListCreateAPIView):
    #Clase que se encraga de retornar todos lo elementos por medio del serializcer
    queryset = NewVideo.objects.all()
    serializer_class = NewVideoSerializer

def getMoodData(*args, **kwargs):
    '''La función se encarga de realizar una consulya a la DB y extraer
    elementos que cumplan com una emocion determinada

    Args:
        *args: Es una tupla de parámetros posicionales
        **kwargs: Es un diccionario de parametros con nombre
        
    Returns:
        Json:Con los valore ya filtrados.
    '''
    #numberMood = switch(kwargs.get('mood'))
    mood = kwargs.get('mood')
    queryset = NewVideo.objects.filter(predicted_moods__iexact=mood)
    data = list(queryset.values("video_id", "video_title", "predicted_moods", "video_type"))
    return JsonResponse(data, safe=False)

def getMoodGenreData(*args, **kwargs):
    '''La función se encarga de realizar una consulya a la DB y extraer
    elementos que cumplan com una emocion y género determinado.

    Args:
        *args: Es una tupla de parámetros posicionales
        **kwargs: Es un diccionario de parametros con nombre
        
    Returns:
        Json:Con los valore ya filtrados.
    '''
    #numberMood = switch(kwargs.get('mood'))
    mood = kwargs.get('mood')
    genero = kwargs.get('genre')
    queryset = NewVideo.objects.filter(predicted_moods__iexact=mood).filter(video_type__iexact=genero)
    data = list(queryset.values('video_id', 'video_title', 'predicted_moods', "video_type"))
    return JsonResponse(data, safe=False)

def getNameData(*args, **kwargs):
    '''La función se encarga de realizar una consulta a la DB y extraer
    elementos que cumplan o contengan parte del nombre que se le pasa por parámetro.

    Args:
        *args: Es una tupla de parámetros posicionales
        **kwargs: Es un diccionario de parametros con nombre
        
    Returns:
        Json:Con los valore ya filtrados.
    '''
    name = kwargs.get('name')
    queryset = NewVideo.objects.filter(video_title__icontains=name)
    data = list(queryset.values('video_id', 'video_title', 'predicted_moods', "video_type"))
    return JsonResponse(data, safe=False)