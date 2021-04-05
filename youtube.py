import googleapiclient.discovery
import ytkeys

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = ytkeys.API_KEY

youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)



def GetchannelInfo(channelId):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channelId
    )
    response = request.execute()
    return response


def Getplaylistid(response):
   for item in response['items']:
     return item['contentDetails']['relatedPlaylists']['uploads']


def Getplaylist(plid):
    request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId = plid

    )
    return request.execute()

def Getvideoid(response):
    return response['items'][0]['contentDetails']['videoId']




    