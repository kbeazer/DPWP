'''
Kareem K. Beazer
9/18/14
Design Patterns for Web Programming - Online
Encapsulated
'''

import webapp2
import os
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
        success = Success().print_out()
        self.response.write(h.print_out())


        if self.request.GET:
            #stores the information received from the form
            #name = self.request.GET['name']
            view = self.request.GET['platform']
            os.system('clear')
            self.response.write(success + view)
        else:
            self.response.write(self.error) #prints out the information on the screen

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
