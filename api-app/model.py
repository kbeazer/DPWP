import urllib2
import json


class WunderModel(object):
    """ this Model is in charge of requesting, parsing, and sending data from the Wiki API """
    def __init__(self):
        self.__url = 'http://api.wunderground.com/api/4368eaeb87521ad2/forecast/geolookup/conditions/q/'
        self.__search = ''
        self._mobjects = []

    def call_api(self):
        # assemble the request
        request = urllib2.Request(self.__url + self.__search + '.json')
        # use the urllib2 to create an object to get the url
        opener = urllib2.build_opener()
        # use the url to get a result - request info from the API
        result = opener.open(request)
        # parsing the json
        jsondoc = json.load(result)

        data = WunderData()
        data.updated = jsondoc['current_observation']['observation_time']
        data.name = jsondoc['current_observation']['display_location']['full']
        data.condition = jsondoc['current_observation']['weather']
        data.temperature = jsondoc['current_observation']['temperature_string']
        data.forecast = jsondoc['current_observation']['nowcast']
        data.current = jsondoc['forecast']['txt_forecast']['forecastday'][0]['title']
        data.curmess = jsondoc['forecast']['txt_forecast']['forecastday'][0]['fcttext']
        self._mobjects.append(data)

        """
        print data.name
        print data.condition
        print data.updated
        print data.temperature
        print data.forecast
        """

    @property
    def name(self):
        return self.name

    @property
    def search(self):
        pass

    @search.setter
    def search(self, s):
        self.__search = s


class WunderData(object):
    """ this data object holds the data fetched by the model and shown by the view """
    def __init__(self):
        self.updated = ''
        self.name = ''
        self.condition = ''
        self.temperature = ''
        self.forecast = ''
        self.current = ''
        self.curmess = ''
        self.day1 = ''
        self.d1mess = ''
        self.day2 = ''
        self.d2mess = ''
        self.day3 = ''
        self.d3mess = ''
