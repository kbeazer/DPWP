"""
Kareem K. Beazer
9/20/14
Design Patterns for Web Programming - Online
POC
"""

import webapp2
from gStop import GameGrab
from gStop import ResultsView


class MainHandler(webapp2.RequestHandler):
    def get(self):
        g = GameGrab()
        r = ResultsView()
        self.response.write(g.print_page())
        results = self.request.get('results')
        view = self.request.get('user')

        if view == "":
            self.response.write('Please enter a search query to continue.')
        else:
            self.response.write('You just searched for: ' + view)
            self.response.write(r.print_page())

        if results:
            self.response.write('I work!!!!')
        else:
            pass


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
