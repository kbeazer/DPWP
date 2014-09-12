class Welcome(object):
    def __init__(self):
        self.title = "Welcome!"
        self.css = "css/style.css"
        self.head =  """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>"""
        self.error = '''<p>Please fill out all fields to continue.</p>'''

        self.body = '''<h1>What's The Buzz</h1>
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



        self.close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all
