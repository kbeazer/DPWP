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
from classes import Success

class MainHandler(webapp2.RequestHandler):
    def get(self):
        h = HomePage()
        x1 = Xbox1()
        ps4 = PS4()
        success = Success()
        self.response.write(h.print_out())


        if self.request.GET:
            #stores the information received from the form
            user = self.request.GET['user']
            self.response.write(user + "," + " " + s.print_out())
        else:
            self.response.write(self.error) #prints out the information on the screen

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
