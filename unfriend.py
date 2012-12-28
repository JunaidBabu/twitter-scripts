#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This script will unfriend everyone on a Twitter account.
# Use this script to unfollow all of the people who aren't
# following you.

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
  print 'Thank you for using my unfriend script. - iepathos'
  start = time.time()
  i = 0
  friends = api.friends()
  me = api.me()

  try:
    for friend in friends:
      if api.exists_friendship(friend.id, me.id):
        api.destroy_friendship(friend.id)
        print 'Unfollowed %s' % (friend.name)
        i += 1

        if i % 8 == 0:
          print 'Waiting 60 seconds between next unfollow every 8 unfollows \nbecause Twitter doesn\'t like spammers. Clients allowed only 350 requests every hour.'
          time.sleep(60)
  except ValueError:
    print 'Twitter is unhappy with us.'

  elapsed = time.time() -  start
  print 'Deleted %s non-friends in %s seconds' % (str(i), str(elapsed))
