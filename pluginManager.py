

class Plugin:
    name = ""
    bindings = {}

    def __init__(self, name, bindigns):
        self.name = name
        self.bindings = bindigns

    def get_name(self):
        return self.name

    def get_bindings(self):
        return self.bindings


class PluginManager:
    plugins = {}

    def __init__(self, mediator):
        self.mediator = mediator
        print("Plugin manager created")

    def register_plugin(self, plugin):
        self.plugins[plugin.get_name()] = plugin
        event_engine = self.mediator.get_event_engine()
        event_engine.add_plugin(plugin.get_name, plugin.get_bindings())
