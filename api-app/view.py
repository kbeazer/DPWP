class WunderView(object):
    """ this class shows the data that will be available to the user """
    def __init__(self):
        self.__sobject = []
        self.__content = '<br />'

    def update(self):
        for obj in self.__sobject:
            self.__content += '<div class="region">' + '<h3 class="lineup">' + obj.name + '</h3>' + \
                              '<p class="lineup update">' + obj.updated + '</p>' + '<br />'
            self.__content += '<p>' + "Weather Conditions: " + obj.condition + '</p>' + '<br />'
            self.__content += '<p>' + "Temperature: " + obj.temperature + '</p>' + '</div>' + '<br />'
            self.__content += '<div class="forecast">' + '<h3>Forecast</h3>' + '<p>' + obj.forecast + '</p>' + \
                              '</div>' + "<br />"
            self.__content += '<div class="4-column">' + '<h3 class="title">4-Day Forecast</h3>' + "<br />"
            self.__content += '<div class="current column">' + '<p>' + '<strong>' + obj.current + '</strong>' + \
                              '</p>' + "<br />"

            if obj.curimg == "sunny":
                self.__content += '<img src="images/sunny.png" class="image" />' + '<br />'
            elif obj.curimg == "cloudy":
                self.__content += '<img src="images/cloudy.png" class="image" />' + '<br />'
            elif obj.curimg == "chancetstorms":
                self.__content += '<img src="images/chancetstorms.png" class="image" />' + '<br />'
            elif obj.curimg == "tstorms":
                self.__content += '<img src="images/tstorms.png" class="image" />' + '<br />'
            elif obj.curimg == "chancerain":
                self.__content += '<img src="images/chancerain.png" class="image" />' + '<br />'
            elif obj.curimg == "partlycloudy":
                self.__content += '<img src="images/partlycloudy.png" class="image" />' + '<br />'
            elif obj.curimg == "mostlycloudy":
                self.__content += '<img src="images/partlycloudy.png" class="image" />' + '<br />'
            else:
                print obj.curimg

            self.__content += '<p class="message">' + obj.curmess + '</p>' + '</div>' + "<br />"

            self.__content += '<div class="day1 column">' + '<p>' + '<strong>' + obj.day1 + '</strong>' +\
                              '</p>' + '<br />'

            if obj.d1img == "sunny":
                self.__content += '<img src="images/sunny.png" class="image" />' + '<br />'
            elif obj.d1img == "cloudy":
                self.__content += '<img src="images/cloudy.png" class="image" />' + '<br />'
            elif obj.d1img == "chancetstorms":
                self.__content += '<img src="images/chancetstorms.png" class="image" />' + '<br />'
            elif obj.d1img == "tstorms":
                self.__content += '<img src="images/tstorms.png" class="image" />' + '<br />'
            elif obj.d1img == "chancerain":
                self.__content += '<img src="images/chancerain.png" class="image" />' + '<br />'
            elif obj.d1img == "partlycloudy":
                self.__content += '<img src="images/partlycloudy.png" class="image" />' + '<br />'
            elif obj.d1img == "mostlycloudy":
                self.__content += '<img src="images/partlycloudy.png" class="image" />' + '<br />'
            else:
                print obj.d1img

            self.__content += '<p class="message">' + obj.d1mess + '</p>' + '</div>' + "<br />"

            self.__content += '<div class="day2 column">' + '<p>' + '<strong>' + obj.day2 + '</strong>' + \
                              '</p>' + '<br />'

            if obj.d2img == "sunny":
                self.__content += '<img src="images/sunny.png" class="image" />' + '<br />'
            elif obj.d2img == "cloudy":
                self.__content += '<img src="images/cloudy.png" class="image" />' + '<br />'
            elif obj.d2img == "chancetstorms":
                self.__content += '<img src="images/chancetstorms.png" class="image" />' + '<br />'
            elif obj.d2img == "tstorms":
                self.__content += '<img src="images/tstorms.png" class="image" />' + '<br />'
            elif obj.d2img == "chancerain":
                self.__content += '<img src="images/chancerain.png" class="image" />' + '<br />'
            elif obj.d2img == "partlycloudy":
                self.__content += '<img src="images/partlycloudy.png" class="image" />' + '<br />'
            elif obj.d2img == "mostlycloudy":
                self.__content += '<img src="images/partlycloudy.png" class="image" />' + '<br />'
            else:
                print obj.d2img

            self.__content += '<p class="message">' + obj.d2mess + '</p>' + '</div>' + "<br />"

            self.__content += '<div class="day3 column">' + '<p>' + '<strong>' + obj.day3 + '</strong>' + \
                              '</p>' + '<br />'

            if obj.d3img == "sunny":
                self.__content += '<img src="images/sunny.png" class="image" />' + '<br />'
            elif obj.d3img == "cloudy":
                self.__content += '<img src="images/cloudy.png" class="image" />' + '<br />'
            elif obj.d3img == "chancetstorms":
                self.__content += '<img src="images/chancetstorms.png" class="image" />' + '<br />'
            elif obj.d3img == "tstorms":
                self.__content += '<img src="images/tstorms.png" class="image" />' + '<br />'
            elif obj.d3img == "chancerain":
                self.__content += '<img src="images/chancerain.png" class="image" />' + '<br />'
            elif obj.d3img == "partlycloudy":
                self.__content += '<img src="images/partlycloudy.png" class="image" />' + '<br />'
            elif obj.d3img == "mostlycloudy":
                self.__content += '<img src="images/partlycloudy.png" class="image" />' + '<br />'
            else:
                print obj.d3img

            self.__content += '<p class="message">' + obj.d3mess + '</p>' + '</div>' + '</div>' + '<br />'

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


