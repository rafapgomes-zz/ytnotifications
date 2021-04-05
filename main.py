import youtube
import twitter


twitter_id ='1371881979252252681'
youtube_id = "UCwMiGkjaLWcQn-XXvyQtW0A"

def getytvideoid(yt_id):
    response = youtube.GetchannelInfo(yt_id)
    number = youtube.Getplaylistid(response)
    videos_res = youtube.Getplaylist(number)
    video = youtube.Getvideoid(videos_res)
    return video


def posttweet(tt_id):
    timeline = twitter.searchownTL(tt_id)
    vetor = []
    vetor = twitter.getvideourl(timeline)
    split = []
    split = twitter.splitvetor(vetor)
    for  vid_id in split:
        if getytvideoid(youtube_id) != vid_id:
            texto = 'https://www.youtube.com/watch?v='+ getytvideoid(youtube_id)
            twitter.posttweet(texto)
            return
        else: 
            print('Video nao enviado')
            return

            

posttweet(twitter_id)

