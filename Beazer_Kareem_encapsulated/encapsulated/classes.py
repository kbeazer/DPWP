class HomePage(object):
    def __init__(self):
        self.title = "Gamers World"
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

        self.body = """
        <div>
            <h1>Compare and Select</h1>
            <p>Find a product that best suits your financial needs.</p>
        </div>

        <nav>
            <ul>
                <li>XBox1</li>
                <li>PS4</li>
                <li>Wii U</li>
                <li>XBox 360</li>
                <li>PS3</li>
            </ul>
        </nav>
        <div></div>
        <div></div>

        """
        self.close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

