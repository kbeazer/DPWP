class WunderView(object):
    """ this class shows the data that will be available to the user """
    def __init__(self):
        self.__sobject = []
        self.__content = '<br />'

    def update(self):
        for obj in self.__sobject:
            self.__content += obj.updated + "<br />"
            self.__content += "    LOCATION: " + obj.name + "<br />"
            self.__content += "    CONDITION: " + obj.condition + '<br />'
            self.__content += "   TEMPERATURE: " + obj.temperature + "<br />"
            self.__content += "   FORECAST: " + obj.forecast + "<br />"
            self.__content += "  4-DAY FORECAST" + "<br />"
            self.__content += obj.current + "<br />"
            self.__content += obj.curmess + "<br />"

            if obj.curimg == "sunny":
                self.__content += '<img src="images/sunny.png" />' + '<br />'
            elif obj.curimg == "cloudy":
                self.__content += '<img src="images/cloudy.png" />' + '<br />'
            elif obj.curimg == "chancetstorms":
                self.__content += '<img src="images/chancetstorms.png" />' + '<br />'
            elif obj.curimg == "tstorms":
                self.__content += '<img src="images/tstorms.png" />' + '<br />'
            elif obj.curimg == "chancerain":
                self.__content += '<img src="images/chancerain.png" />' + '<br />'
            elif obj.curimg == "partlycloudy":
                self.__content += '<img src="images/partlycloudy.png" />' + '<br />'
            else:
                print obj.curimg

            self.__content += obj.day1 + "<br />"
            self.__content += obj.d1mess + "<br />"

            if obj.d1img == "sunny":
                self.__content += '<img src="images/sunny.png" />' + '<br />'
            elif obj.d1img == "cloudy":
                self.__content += '<img src="images/cloudy.png" />' + '<br />'
            elif obj.d1img == "chancetstorms":
                self.__content += '<img src="images/chancetstorms.png" />' + '<br />'
            elif obj.d1img == "tstorms":
                self.__content += '<img src="images/tstorms.png" />' + '<br />'
            elif obj.d1img == "chancerain":
                self.__content += '<img src="images/chancerain.png" />' + '<br />'
            elif obj.d1img == "partlycloudy":
                self.__content += '<img src="images/partlycloudy.png" />' + '<br />'
            else:
                print obj.d1img

            self.__content += obj.day2 + "<br />"
            self.__content += obj.d2mess + "<br />"

            if obj.d2img == "sunny":
                self.__content += '<img src="images/sunny.png />' + '<br />'
            elif obj.d2img == "cloudy":
                self.__content += '<img src="images/cloudy.png />' + '<br />'
            elif obj.d2img == "chancetstorms":
                self.__content += '<img src="images/chancetstorms.png />' + '<br />'
            elif obj.d2img == "tstorms":
                self.__content += '<img src="images/tstorms.png />' + '<br />'
            elif obj.d2img == "chancerain":
                self.__content += '<img src="images/chancerain.png" />' + '<br />'
            elif obj.d2img == "partlycloudy":
                self.__content += '<img src="images/partlycloudy.png" />' + '<br />'
            else:
                print obj.d2img

            self.__content += obj.day3 + "<br />"
            self.__content += obj.d3mess + "<br />"

            if obj.d3img == "sunny":
                self.__content += '<img src="images/sunny.png" />' + '<br />'
            elif obj.d3img == "cloudy":
                self.__content += '<img src="images/cloudy.png" />' + '<br />'
            elif obj.d3img == "chancetstorms":
                self.__content += '<img src="images/chancetstorms.png" />' + '<br />'
            elif obj.d3img == "tstorms":
                self.__content += '<img src="images/tstorms.png" />' + '<br />'
            elif obj.d3img == "chancerain":
                self.__content += '<img src="images/chancerain.png" />' + '<br />'
            elif obj.d3img == "partlycloudy":
                self.__content += '<img src="images/partlycloudy.png" />' + '<br />'
            else:
                print obj.d3img

    @property
    def content(self):
        return self.__content

    @property
    def sobject(self):
        pass

    @sobject.setter
    def sobject(self, arr):
        self.__sobject = arr
        self.update()


