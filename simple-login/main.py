'''
Kareem K. Beazer
9/10/14
Design Patterns for Web Programming - Online
Simple Form
'''

import webapp2
from pages import Welcome
from pages import Sucess

class MainHandler(webapp2.RequestHandler):
    def get(self):
        w = Welcome()
        s = Sucess()
        self.response.write(w.print_out())


        if self.request.GET:
            #stores the information received from the form
            user = self.request.GET['user']
            self.response.write(user + "," + " " + s.print_out())
        else:
            self.response.write(self.error) #prints out the information on the screen


#Never touch or modify this code
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
