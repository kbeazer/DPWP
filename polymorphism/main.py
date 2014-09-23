"""
Kareem K. Beazer
9/20/14
Design Patterns for Web Programming - Online
Polymorphism
"""
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['first_name', 'text', 'First Name'], ['last_name', 'text', 'Last Name'], ['Submit', 'submit']]
        self.response.write(p.print_out())


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
        self._body = "Filler"
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
