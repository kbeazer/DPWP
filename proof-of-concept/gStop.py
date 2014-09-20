class GameGrab(object):
    def __init__(self):
        self.input = ""
        self.title = "Game Grabber"
        self.css = "css/style.css"
        self.head = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>{self.title}</title>
                <link href="{self.css}" rel="stylesheet" type="css/text" />
            </head>
            <body>
                <h1>The Video Game Grabber</h1>
                <h2>The one stop center for all your gaming needs.</h2>
                <form method="GET" action="http://www.google.com/search">
                    <input type="hidden" name="sitesearch" value="{self.input}" />
                    <input type="text" placeholder="enter your search here" />
                    <input type="submit" value="Search" />
                </form>
        """
        self.close = """
            </body>
        </html>

        """


    def print_page(self):
        page = self.head + self.close
        return page