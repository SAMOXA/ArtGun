from unittest import TestCase
from appMediator import AppMediator
from pluginManager import Plugin
from pluginManager import PluginAlreadyExist
from interfaceManager import BaseInterface
from interfaces.messages.baseMsg import BaseMsg


class TestPluginManager(TestCase):
    def test_plugin_manager_base(self):
        class TestMessage(BaseMsg):
            def __init__(self):
                super().__init__('TestMessage', '1', '2', 100)

        class TestMessageTwoFields(BaseMsg):
            def __init__(self, arg1, arg2):
                super().__init__('TestMessageTwoFields', '1', '2', 100)
                self.version_fields['0.0'] = ['test1', 'test2']
                self.add_specific_fields(['test1', 'test2'])
                self.fields['test1'] = arg1
                self.set_field('test2', arg2)

        class TestMessageThreeFields(BaseMsg):
            def __init__(self, arg1, arg2, arg3):
                super().__init__('TestMessageThreeFields', '1', '2', 100)
                self.version_fields['0.0'] = ['test1', 'test2', 'test3']
                self.add_specific_fields(['test1', 'test2', 'test3'])
                self.set_field('test1', arg1)
                self.set_field('test2', arg2)
                self.set_field('test3', arg3)

        mediator = AppMediator()

        test_method1 = lambda: "test_method1"
        test_method_args = (lambda x, y: x + y)
        test_method_revers = (lambda a, b, c: str(a) + str(b) + str(c))
        test_one_way_method_output = ''
        def test_one_way_method(arg1):
            global test_one_way_method_output
            test_method_revers_output = str(arg1) + 'pass'

        methods = {
            "test_method1": 'TestMessage',
            "test_method_args": 'TestMessageTwoFields',
            "test_method_reverse_args": 'TestMessageTwoFields'
        }
        interface = BaseInterface("test_interface", methods)

        test_method_revers_output = ''
        test_method_args_output = 0

        def test_method_args_callback(result):
            global test_method_args_output
            test_method_args_output = result + 2

        def test_method_revers_callback(result, test2):
            global test_method_revers_output
            test_method_revers_output = result + test2

        #Test no return
        #Test no return callback
        #Test return
        #Test return callback

        bindings = {
            "test_interface": {
                "test_method1": {
                    'fn': test_method1,
                    'bindings': [],
                },
                "test_method_args": {
                    'fn': test_method_args,
                    'bindings': ['test1', 'test2'],
                    'callback': test_method_args_callback,
                    'callback_bindings': ['result']
                },
                "test_method_reverse_args": {
                    'fn': test_method_revers,
                    'bindings': ['test3', 'test2', 'test1'],
                    'callback': test_method_revers_callback,
                    'callback_bindings': ['result', 'test2']
                }
            }
        }
        plugin = Plugin("test_plugin", bindings)

        i = mediator.get_interface_manager()
        i.add_interface(interface)

        p = mediator.get_plugin_manager()
        p.register_plugin(plugin)

        msg1 = TestMessage()
        result = interface.call_method("test_method1", msg1)
        self.assertEqual(result, "test_method1")

        msg2 = TestMessageTwoFields(2, 2)
        result = interface.call_method("test_method_args", msg2)
        self.assertEqual(result, 4)

        msg3 = TestMessageThreeFields('a', 'b', 'c')
        result = interface.call_method("test_method_reverse_args", msg3)
        self.assertEqual(result, 'cba')

    def test_add_same_plugin(self):
        mediator = AppMediator()

        test_method1 = lambda: "test_method1"
        test_method_args = (lambda x, y: x + y)

        methods = {
            "test_method1": 'TestMessage',
            "test_method_args": 'TestMessageTwoFields'
        }
        interface = BaseInterface("test_interface", methods)

        bindings = {
            "test_interface": {
                "test_method1": {
                    'fn': test_method1,
                    'bindings': []
                },
                "test_method_args": {
                    'fn': test_method_args,
                    'bindings': ['test1', 'test2']
                },
            }
        }
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


