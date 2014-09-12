class Welcome(object):
    def __init__(self):
        self.title = "The Buzz"
        self.css = "css/style.css"
        self.head =  """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>"""
        self.body = '''<h1>What's The Buzz</h1>
        <h2>Find out what events are going down in your city.</h2>
        <h3>Sign up and get access today. Don't miss out!</h3>
        <form method="GET">
            <label>User Name</label>
            <input type="text" name="user" required/>
            <label class="spacer">Gender</label>
            <input type="radio"  name="gender" value="male" /><label class="inline">Male</label>
            <input type="radio"  name="gender" value="female" /><label class="inline">Female</label>
            <label class="spacer">City</label>
            <input type="text" name="city" />
            <label class="spacer">Preferred Genre</label>
            <input type="checkbox" value="Hip Hop" /><p class="inline">Hip Hop</p>
            <input type="checkbox" value="RnB" /><p class="inline">RnB</p>
            <input type="checkbox" value="Jazz" /><p class="inline">Jazz</p>
            <input type="checkbox" value="Reggae" /><p class="inline">Reggae</p>
            <input type="checkbox" value="Dance" /><p class="inline">Dance</p>
            <label class="spacer">Password</label>
            <input type="password" />
            <label>Confirm</label>
            <input type="password" />
            <input class="spacer button" type="submit" value="Submit" />
        </form>
        '''

        self.close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all


class Sucess(object):
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
    <body>
        """

        self.body = "Welcome to the Buzz community!!"
        self.close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all