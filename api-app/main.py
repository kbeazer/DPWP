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
    """ this is the main handler class/catalyst """
    def get(self):
        f = UserForm()  # assign User Form class to a variable
        f.inputs = [['zip', 'text', 'enter a zipcode'], ['Submit', 'submit']]  # array to hold user input

        if self.request.GET:  # only if there is a zip variable in the url

            m = WunderModel()  # creates the Model
            m.search = self.request.GET['zip']  # sends the zipcode from the url to the model
            m.call_api()  # connect to the API

            v = WunderView()  # creates the user View
            v.sobject = m._mobjects  # takes the data objects from the Model class and sends them to the View
            f._body = v.content

        self.response.write(f.print_out())  # print out the result of the User Form class to the view


class Page(object):
    """ this class is used as a template to display the results from the User Form """
    def __init__(self):  # constructor function
        self.title = "Dotlent Weather"  # assign title to attribute
        self.css = "css/style.css"  # assign the css file to attribute
        self._head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
        <link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=PT+Sans+Narrow' rel='stylesheet' type='text/css'>
    </head>
    <body>
        <div id="container">
            <img src="images/wedback.jpg" class="background" height="200" />
            <h1>WundaWeath Application</h1>
            <h2>Find out current weather conditions in your city.</h2>
        </div>
        """
        self._body = ""
        self._close = """
        <footer><p>WundaWeath 2014 &copy</p></footer>
    </body>
</html>
        """

    def print_out(self):
        all = self._head + self._body + self._close  # concatenate entire page into 1 variable
        all = all.format(**locals())
        return all


class UserForm(Page):  # THIS USER FORM CLASS INHERITS THE ATTRIBUTES OF THE PAGE CLASS.
    """ this class is used to store the user input  """
    def __init__(self):
        super(UserForm, self).__init__()  # Page.__init__()
        # create a form to hold user inputs
        self._form_open = '<div class="userInput">' + '<form method="GET">'
        self._form_close = '</form>' + '</div>'
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
                self._form_inputs += '" placeholder="' + i[2] + '" required />'
            # else...end the closing tag
            except:
                self._form_inputs += '" required />'

    # THIS PRINTOUT USES POLYMORPHIS BY OVERRIDING THE PRINT FEATURE OF ITS PARENT CLASS (PAGE).
    def print_out(self):
        all = self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close
        all = all.format(**locals())
        return all


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
