'''
Kareem K. Beazer
9/18/14
Design Patterns for Web Programming - Online
Encapsulated
'''

import webapp2  # imports the webapp2 application
from classes import HomePage   # imports homepage function
from classes import Success  # imports the success message function
from classes import Xbox1

class MainHandler(webapp2.RequestHandler):
    def get(self):
        h = HomePage()  # set homepage function to variable
        success = Success().print_out()  # set success function to variable
        self.response.write(h.print_out())  # prints results


        if self.request.GET:  # stores the information received from the form
            view = self.request.GET['platform']  # assign the view to a variable
            self.response.write(success + view)
        else:
            pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
