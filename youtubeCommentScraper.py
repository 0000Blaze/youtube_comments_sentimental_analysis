#code to retrive youtube comments of a video from the Google provided youtube API
#requires google cloud developers account and a API with enabled youtube data API
#pip install --upgrade google-api-python-client

import os
import googleapiclient.discovery
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

def get_comments(youtube,PageToken=""):
    request = youtube.commentThreads().list(
        part="snippet",
        order="time",
        pageToken = PageToken,
        # videoId="YRvf00NooN8"   #Elon Musk: A future worth getting excited about | TED | Tesla Texas Gigafactory interview
        videoId="JGwWNGJdvx8"   #Ed Sheeran - Shape of You (Official Music Video)           
    )
    response = request.execute()
    return response

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv('GOOGLE_API_KEY')     #api key from .env file 

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    PageToken=""
    all_comments =[]
    numberOfComments = 16000     #divisible by 20 as each batch retrives 20 comments
    num=0
# loop for continous retrival
    while (num<numberOfComments):
        response = get_comments(youtube,PageToken)
        num = num + 20

        PageToken = response['nextPageToken']
        
        for i in range(len(response['items'])):        
            data = dict(Author = response ['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                        Comment = response ['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay'],
                        Publish_Date = response ['items'][i]['snippet']['topLevelComment']['snippet']['publishedAt']
                        )
            all_comments.append(data)

        print("Number of comments retrived: ",num)

    comment_data = pd.DataFrame(all_comments)
    comment_data.to_csv('data.csv',index=False)

if __name__ == "__main__":
    main()