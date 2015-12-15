# This bot follows all current followers
# and suggests to remove friends who do not follow back
import tweepy
from credentials import credentials

# Get credentials from another file
consumer_key = credentials['consumer_key']
consumer_secret = credentials['consumer_secret']
access_token = credentials['access_token']
access_token_secret = credentials['access_token_secret']
my_id = credentials['my_id']

# set credentials and create api object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# create list of followers and following
followers = api.followers_ids(my_id)
friends = api.friends_ids(my_id)

# remove friends who do no follow back
for friend in friends:
    if friend not in followers:
        if raw_input("Unfollow " + str(api.get_user(friend).screen_name) + " (Y/N)? ").lower == 'y':
            api.destroy_friendship(friend)

# add new followers to friends
for follower in followers:
    if follower not in friends:
        print "Following: " + str(api.get_user(follower).screen_name)
        api.create_friendship(follower)
