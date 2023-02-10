import tweepy
from run_model import is_ryan
import time

# I did not want to set up a server, and my application only needs to be running when I want it to be
# This project was to show a friend and I only needed it to be running for a day
# If needed to run all the time, you will need to host it somewhere and have a listener running
running = True
while running:
    API_KEY = "YOUR_API_KEY"
    API_SECRET = "YOUR_API_SECTRET"
    BEARER_TOKEN = "YOUR_BEARER_TOKEN"
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    ACCESS_SECRET = "YOUR_ACCESS_SECRET"
    class TwitterSecrets:
        """Class that holds Twitter Secrets"""

        def __init__(self):
            self.API_KEY    = API_KEY
            self.CONSUMER_SECRET = API_SECRET
            self.ACCESS_TOKEN    = ACCESS_TOKEN
            self.ACCESS_SECRET   = ACCESS_SECRET
            self.BEARER_TOKEN   = BEARER_TOKEN
            
            # Tests if keys are present
            for key, secret in self.__dict__.items():
                assert secret != "", f"Please provide a valid secret for: {key}"

    twitter_secrets = TwitterSecrets()
    consumer_key = twitter_secrets.API_KEY
    consumer_secret = twitter_secrets.API_SECRET
    access_token = twitter_secrets.ACCESS_TOKEN
    access_secret = twitter_secrets.ACCESS_SECRET
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api=tweepy.API(auth)
    def connect_to_twitter():
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api_status = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
        return api_status

    t = open("latest_id.txt", "r")
    latest_id = t.read()
    t.close()
    #api = connect_to_twitter()
    status = api.mentions_timeline()
    obj = status[0]
    id = str(getattr(obj, '_json')['id'])
    user = str(getattr(obj, '_json')['entities']['user_mentions'][0]['id'])
    submitter = str(getattr(obj, '_json')['entities']['user_mentions'][0]['screen_name'])
    if latest_id == id:
        print('skipping')
        pass
    else:
        f = open("latest_id.txt", "w")
        f.write(id)
        f.close()
        try:
            if user == '334390930':
                api.send_direct_message(recipient_id=user, text="lmao ur so gay")
            elif user == '1585711334003458048':
                api.send_direct_message(recipient_id=user, text="gay")
            pic = (getattr(obj, '_json'))['entities']['media'][0]['media_url_https']
            determine = is_ryan(pic)
        except:
            determine = "no pic was provided"
        api.update_status(determine, in_reply_to_status_id=id, auto_populate_reply_metadata=True)
    time.sleep(45)