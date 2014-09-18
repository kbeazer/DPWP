class HomePage(object):
    def __init__(self):  # generates the home page view.
        self.error = "Please select an option to continue."
        self.title = "Gamers World"  # sets the title attribute for the page.
        self.css = "css/style.css"  # sets the location of the css file.
        self.head = """
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
            <p>Please select a product from the list below.</p>
        </div>

        <nav>
            <ul>
                <li class="heading">XBox 1</li>
                {self.xbox1}
                <li class="heading">PS4</li>
                {self.ps4}
                <li class="heading">Wii U</li>
                {self.wii}
                <li class="heading">XBox 360</li>
                {self.x360}
                <li class="heading">PS3</li>
                {self.ps3}

            </ul>
        </nav>

        <div></div>
        <div></div>

        """
        self.close = """
    </body>
</html>
        """

        self.xbox1 = Xbox1().print_dis()  # add xbox1 print function to class.
        self.ps4 = PS4().print_dis()  # add ps4 print function to class.
        self.wii = Wii().print_dis()  # add wii print function to class.
        self.x360 = Xbox360().print_dis()  # add xbox 360 print function to class.
        self.ps3 = PS3().print_dis()  # add ps3 print function to class.

    def print_out(self):
        all = self.head + self.body + self.close  # stores information into all variable
        all = all.format(**locals())
        return all

class Xbox1(object):
    def __init__(self):
        self.view = "Xbox 1"
        self.display = """
        <ul>
            <li>User Rating:  9.5/10</li>
            <li>Price:  $399.99</li>
            <li>Community:  Large</li>
        </ul>
        """
        self.button = """
        <form method="GET">
            <input type="submit" value="Xbox 1" name="platform" />
        </form>
        """

    def print_dis(self):
        display = self.display + self.button
        return display

class PS4(object):
    def __init__(self):
        self.display = """
        <ul>
            <li>User Rating:  8.0/10</li>
            <li>Price:  $499.99</li>
            <li>Community:  Large</li>
        </ul>
        """
        self.button = """
        <form method="GET">
            <input type="submit" value="PS4" name="platform" />
        </form>
        """
    def print_dis(self):
        display = self.display + self.button
        return display

class Wii(object):
    def __init__(self):
        self.display = """
        <ul>
            <li>User Rating:  7.2/10</li>
            <li>Price:  $299.99</li>
            <li>Community:  Medium</li>
        </ul>
        <form method="GET">
            <input type="submit" value="Wii U" name="platform" />
        </form>

        """

    def print_dis(self):
        display = self.display
        return display

class Xbox360(object):
    def __init__(self):
        self.display = """
        <ul>
            <li>User Rating:  9.3/10</li>
            <li>Price:  $199.99</li>
            <li>Community:  Large</li>
        </ul>
        <form method="GET">
            <input type="submit" value="XBox 360" name="platform" />
        </form>

        """
    def print_dis(self):
        display = self.display
        return display

class PS3(object):
    def __init__(self):
        self.display = """
        <ul>
            <li>User Rating:  9.5/10</li>
            <li>Price:  $149.99</li>
            <li>Community:  Medium</li>
        </ul>
        <form method="GET">
            <input type="submit" value="PS3" name="platform" />
        </form>

        """
    def print_dis(self):
        display = self.display
        return display

class Success(object):
    def __init__(self):
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
            <h1>Your Selection</h1>
            <p>You have selected the :</p>
        </div>

        """
        self.close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all