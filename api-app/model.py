class WikiModel(object):
    """ this Model is in charge of requesting, parsing, and sending data from the Wiki API """
    def __init__(self):
        self.__sUrl = "http://en.wikipedia.org/w/api.php?format=json&action=query"
        self.__eUrl = "&prop=revisions&rvprop=content"
        self.__search = ''  # needs & before variable and %20 between any spaces

    def call_api(self):

        # assemble the request
        request = urllib2.Request(self.__sUrl + '&' + self.__search + self.__eUrl)
        # use the urllib2 to create an object to get the url
        opener = urllib2.build_opener()
        # use the url to get a result - request info from the API
        result = opener.open(request)

        # parsing the json
        jsondoc = json.load(result)

        name = jsondoc

        self.response.write(name)
