# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
CK = 'Nz1uSmTlnSdUdn5AXpPYc5QJr'
CS = 'sg6w293jm4BbvnfkBJDkattHlSSgPWeNoquCUacmZm6MA3Ydo0'
AT = ''
AS = ''

url = "https://api.twitter.com/1.1/statuses/update.json"
params = {"status": "テスト"}

twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

if req.status_code == 200:
  print ("OK")
else:
  print ("Error: %d" % req.status_code)
