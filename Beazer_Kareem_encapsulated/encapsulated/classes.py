class HomePage(object):
    def __init__(self):  # generates the home page view.
        self.title = "Gamers World"  # sets the title attribute for the page.
        self.css = "css/style.css"  # sets the location of the css file.
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
                <li>XBox 1</li>
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

class Xbox1(object):
    def __init__(self):
        self.display = """
        <ul>
            <li>User Rating:  9.5/10</li>
            <li>Price:  $399.99</li>
            <li>Community:  Large</li>
        </ul>

        """
    def print_dis(self):
        display = self.display
        return display