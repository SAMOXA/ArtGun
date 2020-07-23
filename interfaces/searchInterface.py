from interfaceManager import BaseInterface


class SearchInterface(BaseInterface):
    def __init__(self):
        methods = set()
        methods.add("SearchByTags")
        methods.add("SearchById")
        super().__init__("SearchInterface", )
        pass
