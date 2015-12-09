# -*- coding: utf-8 -*-

# sample: 100
# precision: 0.71 (estimate)
# recall: 0.83 (estimate)

# todo: returnPlausibleVideoId()の処理がnot smart

import sys
import requests
import json
from requests_oauthlib import OAuth1Session

GOOGLE_API_KEY = 'AIzaSyCgwHYIlfI_Duo5dvQY_aoofV6AUJyMg0M'
TWITTER_CK = 'Nz1uSmTlnSdUdn5AXpPYc5QJr'
TWITTER_CS = 'sg6w293jm4BbvnfkBJDkattHlSSgPWeNoquCUacmZm6MA3Ydo0'
TWITTER_AT = '860724973-ORvMNqqN4oZOnw1bYIPn2T7jLeyhYo9klUad5MJf'
TWITTER_AS = 'wu31x3zWd3yUoj5hZefL9kLtRdGe64jl7nfQ2fw900oBc'

# 曲名でYouTubeから動画リストを所得
def searchSong(keyword):
  url = "https://www.googleapis.com/youtube/v3/search?key=%s&q=%s&part=id&maxResults=3" % (GOOGLE_API_KEY, keyword)
  print "Getting video information from YouTube by querying %s ..." % keyword, 
  response = requests.get(url).json()
  return response

# 動画リストの中から適切なビデオを1つ返す
def returnPlausibleVideoID(response_json):
  # 今は単純にTopの動画idを返すだけ
  try:
    j = response_json.get('items')
    if not j:
      print "Error: Cannot find the song on YouTube",
      return False
    else:
      print "Getting the plausible song url...",
      return j[0]['id']['videoId']
  except:
    print "Error: Argument is not json"

# 曲および動画情報をツイート
def tweetSong(keyword, video_id):
  if video_id == False:
    print "Error: Cannot tweet the song information", 
  else: 
    url = "https://api.twitter.com/1.1/statuses/update.json"
    tweet = "%s youtu.be/%s #nowplaying" % (keyword, video_id)
    params = {"status": tweet}
    twitter = OAuth1Session(TWITTER_CK, TWITTER_CS, TWITTER_AT, TWITTER_AS)
    print "Tweeting the song information...",
    req = twitter.post(url, params = params)
    if req.status_code == 200:
      return True
    else:
      print "Error: %d" % req_status_code,

def main(artist_name, song_name):
  kw = artist_name + " - " + song_name
  r = searchSong(kw)
  song_video_id = returnPlausibleVideoID(r)
  tweetSong(kw, song_video_id)

if __name__ == '__main__':
  artist = sys.argv[1]
  song = sys.argv[2]
  main(artist, song)
