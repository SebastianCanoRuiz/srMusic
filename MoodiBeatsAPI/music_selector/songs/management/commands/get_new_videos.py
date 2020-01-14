from django.core.management.base import BaseCommand

from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
#import requests
import json

from songs.models import NewVideo

load_dotenv()

def html_reverse_escape(string):
    '''Reverse escapes HTML code in string into ASCII text.'''
    # see Ned Batchelder post https://stackoverflow.com/questions/2077283/escape-special-html-characters-in-python
    return (string \
        .replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"'))



def search_api():
    '''Searches YouTube Data API v3 for videos based on project-specified parameters; returns list of videos.'''
    api_service_name = 'youtube'
    api_version = 'v3'
    DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')

    youtube = build(api_service_name, api_version,
                    developerKey = DEVELOPER_KEY)


    #r = requests.get('http://ws.audioscrobbler.com/2.0/?method=track.search&track=Believe&api_key=2e6a35d37b6129caf404f0699e8f7474&format=json')
    #data_string = json.loads(r.content)
    #print (data_string)

    request = youtube.search().list(
        part='id,snippet',
        maxResults=1,
        q='instrumental edm',
        relevanceLanguage='en',
        type='video',
        videoDuration='medium',
        videoLicense='creativeCommon',
        videoSyndicated='true',
    ).execute()

    

    videos = []
    result_count = 0


    for search_result in request['items']:
        video_title         = search_result['snippet']['title']
        video_title         = html_reverse_escape(video_title)
        video_id            = search_result['id']['videoId']
        video_description   = search_result['snippet']['description']
        video_description   = html_reverse_escape(video_description)
        genero = 
      
        try:
            new_videos = NewVideo(
                video_id=video_id,
                video_title=video_title,
                video_description=video_description
            )

            new_videos.save()
        except:
            pass

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Agregando datos de Youtube API al Dataset")
        search_api()