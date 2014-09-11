'''
Kareem K. Beazer
9/10/14
Design Patterns for Web Programming - Online
Simple Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
    <title>What's The Buzz</title>
    </head>
    <body>'''
        page_error = '''<p>Please fill out all fields to continue.</p>'''

        page_body = '''<h1>What's The Buzz</h1>
        <h2>Find out what events are going down in your city.</h2>
        <h3>Sign up and get access today. Don't miss out!</h3>
        <form method="GET">
            <label>User Name</label><br>
            <input type="text" name="user" /><br>
            <label>Gender</label><br>
            <input type="radio"  name="gender" value="male" /> Male<br>
            <input type="radio"  name="gender" value="female" /> Female<br>
            <label>City</label><br>
            <input type="text" name="city" /><br>
            <label>Preferred Genre</label><br>
            <input type="checkbox" value="Hip Hop" /><br>
            <input type="checkbox" value="RnB" /><br>
            <input type="checkbox" value="Jazz" /><br>
            <input type="checkbox" value="Reggae" /><br>
            <input type="checkbox" value="Dance" /><br>
            <input type="submit" value="Submit" />'''

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
