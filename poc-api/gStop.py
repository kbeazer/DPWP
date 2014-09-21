class GameGrab(object): # GameGrab object start
    def __init__(self):
        self.title = "Game Grabber"  # sets the title of the page
        self.css = "css/style.css"  # sets the path of the css directory
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="css/text" />
    </head>
    <body>
        """
        self.body = """
        <div class="container">
            <h1>The Video Game Grabber</h1>
            <h2>The one stop center for all your gaming needs.</h2>
            <form method="GET">
                <input type="text" name="user" />
                <input type="submit" value="Search" name="entry" />
            </form>
        </div>
        """
        self.close = """
    </body>
</html>
        """

    def print_page(self): # print page attribute enabled
        page = self.head + self.body + self.close
        page = page.format(**locals())
        return page


class ResultsView(object):
    def __init__(self):
        self.title = "Game Grabber"
        self.css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="css/text" />
    </head>
    <body>
        """
        self.body = """
       <form method="GET">
            <input type="submit" value="View the Results" name="results" />
        </form>
        """
        self.close = """
    </body>
</html>
        """

    def print_page(self):
        page = self.head + self.body + self.close
        page = page.format(**locals())
        return page


class Redirect(object):
    def new_page(self):
        action = "https://www.google.com/webhp?gws_rd=ssl#q="  # starting link for the search engine
        return action
