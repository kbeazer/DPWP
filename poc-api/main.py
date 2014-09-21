"""
Kareem K. Beazer
9/20/14
Design Patterns for Web Programming - Online
POC
"""

import webapp2
from gStop import GameGrab  # imports the GameGrab class from the gStop.py file
from gStop import ResultsView  # imports the ResultsView class from the gStop.py file
from gStop import Redirect  # imports the Redirect class from the gStop.py file


class MainHandler(webapp2.RequestHandler):
    def get(self):
        g = GameGrab()  # Assigns GameGrab object to a variable.
        r = ResultsView()  # Assigns ResultsView object to a variable.
        direct = Redirect()  # Assigns Redirect object to a variable.
        self.response.write(g.print_page())  # print out home page
        results = self.request.get('results')  # store the results button to a variable
        view = self.request.get('user')  # store the user information to a variable

        if view == "":
            self.response.write('<p>Please enter a search query to continue.</p>')  # error message
        elif view:
            self.response.write('<p>You just searched for: </p>' + view)  # print out user response to screen
            self.response.write(r.print_page())  # enable the view results button

        if results:
            self.response.clear()  # clear screen of current data
            self.redirect(direct.new_page() + view)  # redirect to new page
        else:
            pass


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
