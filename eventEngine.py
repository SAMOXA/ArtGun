from interfaceManager import InterfaceNotExist


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
        interface_manager = self.mediator.get_interface_manager()
        for interface in bindings:
            if interface_manager.have_interface(interface) is False:
                raise InterfaceNotExist(interface, interface_manager.get_interface_list())

            for method in bindings[interface]:
                self.bindings[interface][method][plugin_name] = bindings[interface][method]

    def call_method(self, interface_name, method_name, *args):
        interface_manager = self.mediator.get_interface_manager()
        if interface_manager.have_interface(interface_name) is False:
            raise InterfaceNotExist(interface_name, interface_manager.get_interface_list())

        for plugin in self.bindings[interface_name][method_name]:
            if len(args) == 0:
                return self.bindings[interface_name][method_name][plugin]()
            else:
                return self.bindings[interface_name][method_name][plugin](*args)
