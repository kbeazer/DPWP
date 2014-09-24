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

        data = WunderData()  # store the database in a variable
        # Search through the json api and grab information to send to the view
        data.updated = jsondoc['current_observation']['observation_time']
        data.name = jsondoc['current_observation']['display_location']['full']
        data.condition = jsondoc['current_observation']['weather']
        data.temperature = jsondoc['current_observation']['temperature_string']
        data.forecast = jsondoc['current_observation']['nowcast']
        data.current = jsondoc['forecast']['txt_forecast']['forecastday'][0]['title']
        data.curmess = jsondoc['forecast']['txt_forecast']['forecastday'][0]['fcttext']
        data.curimg = jsondoc['forecast']['txt_forecast']['forecastday'][0]['icon']
        data.day1 = jsondoc['forecast']['txt_forecast']['forecastday'][2]['title']
        data.d1mess = jsondoc['forecast']['txt_forecast']['forecastday'][2]['fcttext']
        data.d1img = jsondoc['forecast']['txt_forecast']['forecastday'][2]['icon']
        data.day2 = jsondoc['forecast']['txt_forecast']['forecastday'][4]['title']
        data.d2mess = jsondoc['forecast']['txt_forecast']['forecastday'][4]['fcttext']
        data.d2img = jsondoc['forecast']['txt_forecast']['forecastday'][4]['icon']
        data.day3 = jsondoc['forecast']['txt_forecast']['forecastday'][6]['title']
        data.d3mess = jsondoc['forecast']['txt_forecast']['forecastday'][6]['fcttext']
        data.d3img = jsondoc['forecast']['txt_forecast']['forecastday'][6]['icon']
        self._mobjects.append(data)  # add data object to the mobjects array

    @property
    def search(self):
        pass

    @search.setter
    def search(self, s):
        self.__search = s


class WunderData(object):  # THIS PAGE CLASS IS AN EXAMPLE OF AN ABSTRACT CLASS.  IT IS BEING USED AS A TEMPLATE.
    """ this data object holds the data fetched by the model and shown by the view """
    def __init__(self):
        self.updated = ''
        self.name = ''
        self.condition = ''
        self.temperature = ''
        self.forecast = ''
        self.current = ''
        self.curmess = ''
        self.curimg = ''
        self.day1 = ''
        self.d1mess = ''
        self.d1img = ''
        self.day2 = ''
        self.d2mess = ''
        self.d2img = ''
        self.day3 = ''
        self.d3mess = ''
        self.d3img = ''
