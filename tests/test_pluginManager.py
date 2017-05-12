from unittest import TestCase
from appMediator import AppMediator
from pluginManager import Plugin
from pluginManager import PluginAlreadyExist
from interfaceManager import Interface

class TestPluginManager(TestCase):
    def test_plugin_manager_base(self):
        mediator = AppMediator()

        test_method1 = lambda: "test_method1"
        test_method_args = (lambda x, y: x + y)

        methods = ["test_method1", "test_method_args"]
        interface = Interface("test_interface", methods)

        bindings = {"test_interface": {"test_method1": test_method1, "test_method_args": test_method_args}}
        plugin = Plugin("test_plugin", bindings)

        i = mediator.get_interface_manager()
        i.add_interface(interface)

        p = mediator.get_plugin_manager()
        p.register_plugin(plugin)

        result = interface.call_method("test_method1")
        self.assertEqual(result, "test_method1")

        result = interface.call_method("test_method_args", 2, 2)
        self.assertEqual(result, 4)

    def test_add_same_plugin(self):
        mediator = AppMediator()

        test_method1 = lambda: "test_method1"
        test_method_args = (lambda x, y: x + y)

        methods = ["test_method1", "test_method_args"]
        interface = Interface("test_interface", methods)

        bindings = {"test_interface": {"test_method1": test_method1, "test_method_args": test_method_args}}
        plugin = Plugin("test_plugin", bindings)
        plugin1 = Plugin("test_plugin", bindings)

        i = mediator.get_interface_manager()
        i.add_interface(interface)

        p = mediator.get_plugin_manager()
        p.register_plugin(plugin)

        try:
            p.register_plugin(plugin1)
        except PluginAlreadyExist as detail:
            self.assertEqual(detail.plugin_name, "test_plugin")


