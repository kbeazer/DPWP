class WunderView(object):
    """ this class shows the data that will be available to the user """
    def __init__(self):
        self.__sobject = []
        self.__content = '<br />'

    def update(self):
        for obj in self.__sobject:
            self.__content += obj.updated + "    LOCATION: " + obj.name + "    CONDITIONS: " + obj.condition
            self.__content += "   TEMPERATURE: " + obj.temperature
            self.__content += "   FORECAST: " + obj.forecast
            self.__content += "  4-DAY FORECAST: " + "<br />"
            self.__content += obj.current + "<br />"
            self.__content += obj.curmess + "<br />"
            self.__content += obj.day1 + "<br />"
            self.__content += obj.d1mess + "<br />"
            self.__content += obj.day2 + "<br />"
            self.__content += obj.d2mess + "<br />"
            self.__content += obj.day3 + "<br />"
            self.__content += obj.d3mess + "<br />"

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
