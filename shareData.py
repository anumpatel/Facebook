# -*- coding: utf-8 -*-

#This script simply uses the Facebook graph API : ref : https://developers.facebook.com/docs/graph-api/reference/v2.8/url
#No access token required for this method. Just pass URL in 'webURL' variable. 
#Data from Json in then fetched and stored in share variable.

import urllib2
import json
from BeautifulSoup import BeautifulSoup


FBURL = "http://graph.facebook.com/?fields=id,share,og_object{likes.summary(true).limit(0)}&id="
webURL = "http://YOUR_URL"
passURL = FBURL + webURL

response = urllib2.urlopen(passURL)
data = json.loads(response.read())
share = data['share']['share_count']
print share
