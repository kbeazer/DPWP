"""
Kareem K. Beazer
9/20/14
Design Patterns for Web Programming - Online
Application with API
"""

import webapp2
import json
import urllib2
from model import WunderModel
from view import WunderView



class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = FormPage()
        f.inputs = [['zip', 'text', 'enter a zipcode'], ['Submit', 'submit']]

        if self.request.GET:  # only if there is a zip variable in the url

            m = WunderModel()  # creates the Model
            m.search = self.request.GET['zip']  # sends the zipcode from the url to the model
            m.call_api()  # connect to the API

            v = WunderView() # creates the user View
            v.sobject = m._mobjects  # takes the data objects from the Model class and sends them to the View
            f._body = v.content

        self.response.write(f.print_out())

class Page(object):
    def __init__(self):
        self._head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>
        """
        self._body = "Find out current weather conditions in your city."
        self._close = """
    </body>
</html>
        """

    def print_out(self):
        return self._head + self._body + self._close


class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()  # Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []  # inputs variable is made private by adding the prefix __
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        # change the inputs variable to be public
        self.__inputs = arr
        # sort through the inputs array and create HTML content based on the information found there.
        for i in arr:
            self._form_inputs += '<input type="' + i[1] + '" name="' + i[0]
            # if there is a third item in array..add it to the array
            try:
                self._form_inputs += '" placeholder="' + i[2] + '" />'
            # else...end the closing tag
            except:
                self._form_inputs += '" />'

        print self._form_inputs

    # Polymorphism Alert--------method overriding
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
