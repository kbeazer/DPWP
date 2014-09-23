class WikiModel(object):
    """ this Model is in charge of requesting, parsing, and sending data from the Wiki API """
    def __init__(self):
        self.__sUrl = "http://en.wikipedia.org/w/api.php?format=json&action=query"
        self.__eUrl = "&prop=revisions&rvprop=content"
        self.__titles = ''  # needs & before variable and %20 between any spaces
