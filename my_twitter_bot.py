#! python
import tweepy
import time
print('This is my twitter bot')
print(' ')


CONSUMER_KEY = 'AAAAAAAAAAA'
CONSUMER_SECRET = 'BBBBBBBB'
ACCESS_KEY = 'CCCCCCCCCCCCC'
ACCESS_SECRET = 'DDDDDDDDDDD'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_totweets():
    print('Retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # usar 1189312810599243777
    mentions = api.mentions_timeline(
                            last_seen_id,
                            tweet_mode='extended')


    for mention in reversed(mentions):
        print(mention.user.screen_name + ' - ' + mention.full_text)
        print(mention.created_at)
        print(mention.id)
        print(' ')
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME) 
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld!')
            print('responding back...')
            api.update_status('@'+ mention.user.screen_name + ' #HelloWorld back to you!!', mention.id )

while True:
        reply_totweets()
        time.sleep(15)
