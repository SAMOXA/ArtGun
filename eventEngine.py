from interfaceManager import InterfaceNotExist
from interfaceManager import InterfaceMethodNotExist


class EventEngine:
    bindings = {}

    def __init__(self, mediator):
        self.mediator = mediator
        self.bindings = {}

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
                if interface_manager.interface_have_method(interface, method) is False:
                    raise InterfaceMethodNotExist(interface, method, interface.get_methods_list())
                self.bindings[interface][method][plugin_name] = bindings[interface][method]

    def call_method(self, interface_name, method_name, msg):
        interface_manager = self.mediator.get_interface_manager()
        if interface_manager.have_interface(interface_name) is False:
            raise InterfaceNotExist(interface_name, interface_manager.get_interface_list())

        for plugin in self.bindings[interface_name][method_name]:
            bindings = self.bindings[interface_name][method_name][plugin]['bindings']
            fn = self.bindings[interface_name][method_name][plugin]['fn']
            if len(bindings) == 0:
                return fn()
            else:
                args_list = list()
                for arg in bindings:
                    args_list.append(msg.get_field(arg))

                return fn(*args_list)
