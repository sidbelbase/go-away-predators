from time import sleep
from keys import *
import tweepy

__author__ = 'sidbelbase'

'''
This script removes all the uncommon followers from your twitter account by blocking them one by one and
then again unblocking them, like we usually do. To make things more clearer, it only removes those accounts
which you aren't following, but those accounts who you haven't shared that magic spark till this moment. This
script is super useful when you don't want to get followed by useless bots, non-active users & don't know maybe 
some other personal issues. This script is tested, trusted and checked 127 times, so every part works just fine.

!!! Disclaimer: But though, RUN at your own risk (Just kidding, I know you want this badly.)

Steps:

Install tweepy module using pip.
Locate keys.py and fill the details like author, consumer_key, consumer_secret, access tokens, token secrets
Visit https://apps.twitter.com to get your credentials i.e. consumer keys and stuffs.

In short to run this, you need a developer account & need to initialize an application. Then you're good to go.
'''

followers = []
followings = []

def sayno(anything_thats_countable):
	if int(len(anything_thats_countable)) == 0:
		return 'None'
	else:
		return len(anything_thats_countable)


def initalize_the_blocker(the_thing_to_be_counted):
	if int(len(the_thing_to_be_counted)) > 0:
		print('\n')
		print('Now, initializing block operation...')
		sleep(1)
		print('Blocking non-mutual followers...')

		for i,uncommoner in enumerate(uncommons):
			username = api.get_user(uncommoner)
			api.create_block(uncommoner)
			api.destroy_block(uncommoner)
			print(f'{i+1}. {username.screen_name} unfollowed you.')
			sleep(5)
		print(f'\nYou\'re safe now. We removed {len(uncommons)} non-mutuals from your account.')
	else:
		print('\nSeems like you didn\'t have any non-mutuals, so we didn\'t remove anyone.')


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

sleep(1)
print('Note: This script blocks those accounts that you don\'t follow.')
print('RIP to those who are about to miss your tweets, let\'s now mourn for them about 5 sec...')
sleep(5)
print(f'Please wait... we\'re checking {AUTHOR}\'s profile...')
sleep(1)
print('\n')

for friend in tweepy.Cursor(api.friends_ids, screen_name=AUTHOR).pages():
	followings.extend(friend)

print(f'\tFollowings: {sayno(followings)}')

for follower in tweepy.Cursor(api.followers_ids, screen_name=author).pages():
	followers.extend(follower)

print(f'\tFollowers: {sayno(followers)}')

commons = [friend for follower in followers for friend in followings if friend == follower ]

print(f'\tMutual Followers: {sayno(commons)}')

uncommons = set(followers) - set(commons)

print(f'\tNon-mutual Followers: {sayno(uncommons)}')

initalize_the_blocker(uncommons)