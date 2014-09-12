'''
Kareem K. Beazer
9/10/14
Design Patterns for Web Programming - Online
Simple Form
'''

import webapp2
#from pages import Welcome

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
    <title>What's The Buzz</title>
    </head>
    <body>'''


        page_close = '''
        </form>
    </body>
</html>'''
        if self.request.GET:
            #stores the information received from the form
            user = self.request.GET['user']
            email = self.request.GET['city']
            self.response.write(page_head + user + ' ' + email + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #prints out the information on the screen

#Never touch or modify this code
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
