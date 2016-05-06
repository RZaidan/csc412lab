import tweepy

##You can learn more about OAuth here: httpa://dev.twitter.com/docs/auth/oauth
consumer_key = 'rdqeS9eZoh1Dqoz55EJFwZabu'
consumer_key_secret = 'U0JgTauTFnjfcMVxdvUf8tVZWLDSPRD8V7Ww1KOIV6ecnaHNCd'
access_token = '721113932836933632-r9vrmi6h1mRSCNXaZbMYmHgBqOx45uJ'
access_token_secret = 'UKCQ4HGCOqNJxGryRl3yE7P2wCxHkD48gLyVTTosZvwHu'


class TweetListener(tweepy.StreamListener):
  def on_status(self, status):
    print('Tweet text: ' + status .text)
    return True

  def on_error(self, status_code):
    print('Got an error with status code: ' + str(status_code))
    return True

  def on_timeout(self):
    print('Timeout..') 
    return True

if __name__ == '__main__':
  listener = TweetListener()
  auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
  auth.set_access_token(access_token, access_token_secret)

  stream = tweepy.Stream(auth, listener)
  stream.filter(follow=[], track=['#SFGiants', '#Athletics']) 
