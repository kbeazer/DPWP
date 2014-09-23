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
            self.__content += "   DAY: " + obj.current + obj.curmess

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
