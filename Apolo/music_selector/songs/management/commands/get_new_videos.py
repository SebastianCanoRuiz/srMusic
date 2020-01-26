from django.core.management.base import BaseCommand
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import json

from songs.models import NewVideo

load_dotenv()

def html_reverse_escape(string):
    ''' Limpia la cadena de emojis, html y cualquier carcater especial ASCII
        Args:  string, la cadena de texto que será limpiada
        Returns: string
    '''
    return (string \
        .replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"'))

def search_api():
    ''' Busca el la YouTube API v3 viideos que cumplan con los parámetros de búsqueda
        
        Returns: lista de video_ids de videos
    '''
    api_service_name = 'youtube'
    api_version = 'v3'
    DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')

    youtube = build(api_service_name, api_version,
                    developerKey = DEVELOPER_KEY)

    """Cadena con la petición de búsqueda, se especifico, usar una licencia CreativeCommons
    para retornar solo videos libres de copyright, y en el parametro q el tipo de busqueda
    para buscar solo canciones de ciertos generos y musicales"""
    request = youtube.search().list(
        part='id,snippet',
        maxResults=1,
        q='music baladas triste',
        relevanceLanguage='en',
        type='video',
        videoDuration='medium',
        videoLicense='creativeCommon',
        videoSyndicated='true',
    ).execute()

    videos = []
    result_count = 0

    #Se ingresan el resultado de búsqueda en el diccionario request
    for search_result in request['items']:
        video_title         = search_result['snippet']['title']
        video_title         = html_reverse_escape(video_title)
        video_id            = search_result['id']['videoId']
        video_description   = search_result['snippet']['description']
        video_description   = html_reverse_escape(video_description)
      
        try:
            new_videos = NewVideo(
                video_id=video_id,
                video_title=video_title,
                video_description=video_description,
                video_type= 'BALADAS',
                predicted_moods='HAPPY'
            )

            new_videos.save()
        except:
            pass

class Command(BaseCommand):
    """Clase que permite ejecutar el comando search_api por medio de linea de comandos,
    para permitir poblar la base de datos con videos musicales, utilizando diferentes parámetros q
    """
    def handle(self, *args, **options):
        print("Agregando datos de Youtube API al Dataset")
        search_api()