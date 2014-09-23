"""
Kareem K. Beazer
9/20/14
Design Patterns for Web Programming - Online
Weather App MVC
"""
import webapp2
import urllib2
from xml.dom import minidom


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'Zip Code'], ['Submit', 'submit']]

        if self.request.GET:  # only if there is a zip variable in the url

            wm = WeatherModel()  # creates the Model
            wm.zip = self.request.GET['zip']  # sends the zipcode from the url to the model
            wm.call_api()  # connect to the API

            wv = WeatherView() # creates the user View
            wv.wdos = wm.dos  # takes the data objects from the Model class and sends them to the View
            p._body = wv.content

        self.response.write(p.print_out())


class WeatherView(object):
    """ this class handles how the data is shown to the user"""
    def __init__(self):
        self.__wdos = []
        self.__content = '<br />'

    def update(self):
        for do in self.__wdos:
            self.__content += do.day + "    HIGH: " + do.high + "    LOW: " + do.low
            self.__content += "   CONDITION: " + do.condition
            self.__content += '<img src="images/' + do.code + '.png" width="20" /><br />'

    @property
    def content(self):
        return self.__content

    @property
    def wdos(self):
        pass

    @wdos.setter
    def wdos(self, arr):
        self.__wdos = arr
        self.update()


class WeatherModel(object):
    """ this model handles fetching, parsing, and sorting data from Yahoo's weather API """
    def __init__(self):
        self.__url = "http://xml.weather.yahoo.com/forecastrss?p="
        self.__zip = ''
        self.__xmldoc = ''
        # parse the URL

    def call_api(self):
        # ---Requests and Loads from the API---
        # assemble the request
        request = urllib2.Request(self.__url + self.__zip)
        # use the urllib2 to create an object to get the url
        opener = urllib2.build_opener()
        # use the url to get a result - request info from the API
        result = opener.open(request)

        # Parsing the Data
        self.__xmldoc = minidom.parse(result)

        # Sorting the Data
        list = self.__xmldoc.getElementsByTagName("yweather:forecast")
        self._dos = []
        for tag in list:
            do = WeatherData()
            do.day = tag.attributes['day'].value
            do.high = tag.attributes['high'].value
            do.low = tag.attributes['low'].value
            do.date = tag.attributes['date'].value
            do.code = tag.attributes['code'].value
            do.condition = tag.attributes['text'].value
            self._dos.append(do)

    @property
    def dos(self):
        return self._dos

    @property
    def zip(self):
        pass

    @zip.setter
    def zip(self, z):
        self.__zip = z


class WeatherData(object):
    """ this data object holds the data fetched by the model and shown by the view """
    def __init__(self):
        self.day = ''
        self.high = ''
        self.low = ''
        self.code = ''
        self.condition = ''
        self.date = ''



class Page(object):
    def __init__(self):
        self._head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>
        """
        self._body = "Weather App"
        self._close = """
    </body>
</html>
        """

    def print_out(self):
        return self._head + self._body + self._close


class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()  # Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []  # inputs variable is made private by adding the prefix __
        self._form_inputs = ''
    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        # change the inputs variable to be public
        self.__inputs = arr
        # sort through the inputs array and create HTML content based on the information found there.
        for i in arr:
            self._form_inputs += '<input type="' + i[1] + '" name="' + i[0]
            # if there is a third item in array..add it to the array
            try:
                self._form_inputs += '" placeholder="' + i[2] + '" />'
            # else...end the closing tag
            except:
                self._form_inputs += '" />'

        print self._form_inputs

    def print_out(self):
        return self._head + "Weather App" + self._form_open + self._form_inputs + self._form_close + self._body + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
