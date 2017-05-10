from unittest import TestCase
from interfaceManager import InterfaceManager
from interfaceManager import Interface
from interfaceManager import InterfaceMethodNotExist
from interfaceManager import InterfaceNotExist


class TestInterface(TestCase):
    def test_interface_base(self):
        test_method1 = lambda: "test_method1"
        test_method_args = (lambda x, y: x + y)

        methods = {"test_method1": test_method1, "test_method_args": test_method_args}
        interface = Interface("test_method1", methods)

        have_func = interface.have_method("test_method1")
        self.assertTrue(have_func)

        have_func = interface.have_method("there_is_no_method")
        self.assertFalse(have_func)

        result = interface.call_method("test_method1")
        self.assertEqual(result, "test_method1")

        result = interface.call_method("test_method_args", 2, 2)
        self.assertEqual(result, 4)

    def test_error_input(self):
        test_method1 = lambda: "test_method1"
        test_method_args = (lambda x, y: x + y)

        methods = {"test_method1": test_method1, "test_method_args": test_method_args}
        interface = Interface("test_interface", methods)

        #Run not existing function
        try:
            interface.call_method("test_method_not_exist")
            self.assertRaises(Exception)
        except InterfaceMethodNotExist as detail:
            self.assertEqual(detail.interface_name, "test_interface")
            self.assertEqual(detail.method_name, "test_method_not_exist")

class TestInterfaceManager(TestCase):
    def test_interface_manager_base(self):
        test_method1 = lambda: "test_method1"
        test_method_args = (lambda x, y: x + y)

        methods = {"test_method1": test_method1, "test_method_args": test_method_args}
        interface = Interface("test_interface", methods)

        i = InterfaceManager()
        i.add_interface(interface)

        have_interface = i.have_interface("test_interface")
        self.assertTrue(have_interface)

        have_interface = i.have_interface("interface_to_not_found")
        self.assertFalse(have_interface)

        have_method = i.interface_have_method("test_interface", "test_method1")
        self.assertTrue(have_method)

        have_method = i.interface_have_method("test_interface", "test_method_not")
        self.assertFalse(have_method)

        returned_interface = i.get_interface("test_interface")
        self.assertEqual(returned_interface, interface)

    def test_error_input(self):
        test_method1 = lambda: "test_method1"
        test_method_args = (lambda x, y: x + y)

        methods = {"test_method1": test_method1, "test_method_args": test_method_args}
        interface = Interface("test_interface", methods)

        i = InterfaceManager()
        i.add_interface(interface)

        try:
            i.get_interface("test_interface_that_not_exist")
            self.assertRaises(Exception)
        except InterfaceNotExist as detail:
            self.assertEqual(detail.interface_name, "test_interface_that_not_exist")
