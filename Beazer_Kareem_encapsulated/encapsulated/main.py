'''
Kareem K. Beazer
9/18/14
Design Patterns for Web Programming - Online
Encapsulated
'''

import webapp2
from classes import HomePage
from classes import Xbox1
from classes import PS4
from classes import Wii
from classes import Xbox360
from classes import PS3

class MainHandler(webapp2.RequestHandler):
    def get(self):
        h = HomePage()
        self.response.write(h.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
