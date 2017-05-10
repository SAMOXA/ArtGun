class InterfaceError(Exception):
    pass


class InterfaceMethodNotExist(InterfaceError):
    method_name = ""
    interface_name = ""
    existing_methods = {}

    def __init__(self, interface_name, method_name, exist_methods):
        self.interface_name = interface_name
        self.method_name = method_name
        self.exist_methods = exist_methods


class InterfaceNotExist(InterfaceError):
    interface_name = ""
    existing_interfaces = {}

    def __init__(self, interface_name, existing_interfaces):
        self.interface_name = interface_name
        self.existing_interfaces = existing_interfaces


class Interface:
    methods = {}
    name = ""

    def __init__(self, name, methods):
        self.methods = methods.copy()
        self.name = name

    def have_method(self, method_name):
        return method_name in self.methods

    def call_method(self, method_name, *args):
        if self.have_method(method_name) == False:
            raise InterfaceMethodNotExist(self.name, method_name, self.methods)

        if len(args) == 0:
            return self.methods[method_name]()
        else:
            return self.methods[method_name](*args)

    def get_interface_name(self):
        return self.name


class InterfaceManager:
    interfaces = {}

    def add_interface(self, interface):
        self.interfaces[interface.get_interface_name()] = interface

    def have_interface(self, interface_name):
        return interface_name in self.interfaces

    def interface_have_method(self, interface_name, method_name):
        return self.interfaces[interface_name].have_method(method_name)

    def get_interface(self, interface_name):
        if self.have_interface(interface_name) == False:
            raise InterfaceNotExist(interface_name, self.interfaces)

        return self.interfaces[interface_name]
