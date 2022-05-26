from youtube_comment_scraper_python import *
import pandas as pd

#open chrome and connenct to video
youtube.open("https://www.youtube.com/watch?v=cdZZpaB2kDM&t=53s")   #Elon Musk talks Twitter, Tesla and how his brain works — live at TED2022
youtube.leypress("pagedown")

data = []
currentpagesource=youtube.get_page_source()
lastpagesource=''

#retrive each comment
while(True):
    if(lastpagesource==currentpagesource):
        break        
    lastpagesource=currentpagesource
    response=youtube.video_comments()

    for c in response['body']:
        data.append(c)    
    youtube.scroll()
    currentpagesource=youtube.get_page_source()

#convert into dataframe and save data as csv
df = pd.DataFrame(data)
df = df.replace('\n',' ', regex=True)
df = df[['Comment', 'Likes']].drop_duplicates(keep="first") 
df.to_csv('data.csv',index=False)