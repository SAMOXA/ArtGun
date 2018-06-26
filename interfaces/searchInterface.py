from interfaceManager import Interface


class SearchInterface(Interface):
    def __init__(self):
        methods = set()
        methods.add("SearchByTags")
        super().__init__("SearchInterface", )
        pass
