"""
Kareem K. Beazer
9/20/14
Design Patterns for Web Programming - Online
Application with API
"""

import webapp2
import json
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
