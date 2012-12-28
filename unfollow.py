#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This script will unfollow everyone on a Twitter account.
# So, only use this if that's what you're interested in.  Use my
# unfriend.py script to only unfollow people who aren't following
# you.

# Written by Glen Baker - iepathos@gmail.com

import tweepy
import time

token_key = ''
token_secret = ''
con_secret = ''
con_key = ''
auth = tweepy.OAuthHandler(con_key, con_secret)
auth.set_access_token(token_key, token_secret)

api = tweepy.API(auth)

if __name__ == '__main__':
  print 'Thank you for using my unfollow script. - iepathos'
  start = time.time()
  i = 0
  friends = api.friends()

  try:
    for friend in friends:
      api.destroy_friendship(friend.id)
      print 'Unfollowed %s' % (friend.name)
      i += 1

      if i % 5 == 0:
        print 'Waiting 60 seconds between next unfollow every 5 unfollows \nbecause Twitter doesn\'t like spammers. Clients allowed only 350 requests every hour. \nSo, about 5.83 unfollows a minute.'
        time.sleep(60)
  except ValueError:
    print 'Twitter is unhappy with us.'

  elapsed = time.time() -  start
  print 'Unfollowed %s people in %s seconds' % (str(i), str(elapsed))
