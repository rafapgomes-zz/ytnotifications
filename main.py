import youtube
import twitter
import time
import threading


twitter_id ='1371881979252252681'
boquinha_id = "UCwMiGkjaLWcQn-XXvyQtW0A"
renato_id = 'UChMJkHCD2wdvSO7CMOuLR-w'
leoruiz_id = 'UCCgZZd8zy-OyiVtQ5WeOV6w'
thyreis_id = 'UCQ0IutRW590TSJUDyBPP2Pw'
gui_id = 'UC_XGgRFoktKUXZVD1_tp7EA'
renan_id = 'UCPJ6Diqv10p-rOfWdKSRs9w'
def getytvideoid(yt_id):
    response = youtube.GetchannelInfo(yt_id)
    number = youtube.Getplaylistid(response)
    videos_res = youtube.Getplaylist(number)
    video = youtube.Getvideoid(videos_res)
    return video

def compara(num,vet):
    print(vet)
    for vid_id in vet:
        if vid_id == num:
            return 1
        

def tweet(name,tt_id,ytbr_id):
    num = getytvideoid(ytbr_id)
    timeline = twitter.searchownTL(tt_id)
    vetor = []
    vetor = twitter.getvideourl(timeline)
    split = []
    split = twitter.splitvetor(vetor)
    teste = compara(num,split)
    if teste != 1:
        twitter.posttweet(name +" postou um novo video "+" https://www.youtube.com/watch?v="+num)
    else:
         print("Video ja enviado")       
            


def main(name,ytbr_id):
        print(name)
        tweet(name,twitter_id,ytbr_id)


while True: 
    main('Renato',renato_id)
    main('Boquinha',boquinha_id)
    main('Leo',leoruiz_id)
    main('Thi',thyreis_id)
    main('Gui',gui_id)
    main('Renan',renan_id)
    time.sleep(60)