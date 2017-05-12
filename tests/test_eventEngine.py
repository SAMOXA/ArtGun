from unittest import TestCase
from appMediator import AppMediator
from interfaceManager import Interface
from pluginManager import Plugin
from interfaceManager import InterfaceMethodNotExist
from interfaceManager import InterfaceMediatorNotSet
from interfaceManager import InterfaceNotExist


class TestEventEngineBase(TestCase):
    def test_event_engine_base(self):
        mediator = AppMediator()

        test_method1 = lambda: "test_method1"
        test_method_args = (lambda x, y: x + y)

        methods = ["test_method1", "test_method_args"]
        interface = Interface("test_interface", methods)

        bindings = {"test_interface": {"test_method1": test_method1, "test_method_args": test_method_args} }
        plugin = Plugin("test_plugin", bindings)

        i = mediator.get_interface_manager()
        i.add_interface(interface)

        p = mediator.get_plugin_manager()
        p.register_plugin(plugin)

        result = interface.call_method("test_method1")
        self.assertEqual(result, "test_method1")

        result = interface.call_method("test_method_args", 2, 2)
        self.assertEqual(result, 4)
        try:
            interface.call_method("test_method_not_exist")
            self.assertRaises(Exception)
        except InterfaceMethodNotExist as detail:
            self.assertEqual(detail.interface_name, "test_interface")
            self.assertEqual(detail.method_name, "test_method_not_exist")

    def test_event_engine_interface_not_exist(self):
        mediator = AppMediator()

        methods = ["test_method1", "test_method_args"]
        interface = Interface("test_interface", methods)

        try:
            interface.call_method("test_method1")
        except InterfaceMediatorNotSet as detail:
            self.assertEqual(detail.interface_name, "test_interface")

        interface.set_mediator(mediator)

        try:
            interface.call_method("test_method1")
        except InterfaceNotExist as detail:
            self.assertEqual(detail.interface_name, "test_interface")
