from pluginManager import PluginManager
from interfaceManager import InterfaceManager
from eventEngine import EventEngine


class AppMediator:
    def __init__(self):
        self.interfaseManager = InterfaceManager(self)
        self.pluginManager = PluginManager(self)
        self.eventEngine = EventEngine(self)

    def get_interface_manager(self):
        return self.interfaseManager

    def get_plugin_manager(self):
        return self.pluginManager

    def get_event_engine(self):
        return self.eventEngine
