class WunderView(object):
    """ this class shows the data that will be available to the user """
    def __init__(self):
        self.__sobject = []
        self.__content = '<br />'

    def update(self):
        for do in self.__sobject:
            self.__content += do.day + "    HIGH: " + do.high + "    LOW: " + do.low
            self.__content += "   CONDITION: " + do.condition
            self.__content += '<img src="images/' + do.code + '.png" width="20" /><br />'

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
