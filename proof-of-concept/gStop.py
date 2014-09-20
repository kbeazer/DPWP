class GameGrab(object):
    def __init__(self):
        self.title = "Game Grabber"
        self.css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}Game Grabber</title>
        <link href="{self.css}" rel="stylesheet" type="css/text" />
    </head>
    <body>
        """
        self.body = """
        <h1>The Video Game Grabber</h1>
        <h2>The one stop center for all your gaming needs.</h2>
        <form method="GET">
            <input type="text" name="user" />
            <input type="submit" value="Search" name="entry" />
        </form>
        """
        self.close = """
    </body>
</html>
        """

    def print_page(self):
        page = self.head + self.body + self.close
        return page


class ResultsView(object):
    def __init__(self):
        self.title = "Game Grabber"
        self.css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}Game Grabber</title>
        <link href="{self.css}" rel="stylesheet" type="css/text" />
    </head>
    <body>
        """
        self.body = """
        <h1>The Video Game Grabber</h1>
        <h2>The one stop center for all your gaming needs.</h2>
        <form method="GET">
            <input type="text" name="user" />
            <input type="submit" value="Search" name="entry" />
        </form>
        """
        self.close = """
    </body>
</html>
        """

    def print_page(self):
        page = self.head + self.body + self.close
        return page