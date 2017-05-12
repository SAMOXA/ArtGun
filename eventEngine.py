from interfaceManager import InterfaceManager
from interfaceManager import Interface


class EventEngine:
    bindings = {}

    def __init__(self, mediator):
        self.mediator = mediator
        self.bindings = {}
        print("EventEngine created")

    def add_interface(self, interface):
        self.bindings[interface.get_interface_name()] = {}
        for method in interface.get_methods_list():
            self.bindings[interface.get_interface_name()][method] = {}

    def add_plugin(self, plugin_name, bindings):
        for interface in bindings:
            for method in bindings[interface]:
                self.bindings[interface][method][plugin_name] = bindings[interface][method]

    def call_method(self, interface_name, method_name, *args):
        for plugin in self.bindings[interface_name][method_name]:
            if len(args) == 0:
                return self.bindings[interface_name][method_name][plugin]()
            else:
                return self.bindings[interface_name][method_name][plugin](*args)
