class PluginError(Exception):
    pass


class PluginAlreadyExist(PluginError):
    plugin_name = ""
    existing_plugins = []

    def __init__(self, plugin_name, existing_plugins):
        self.plugin_name = plugin_name
        self.existing_plugins = existing_plugins


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
        self.plugins = {}

    def register_plugin(self, plugin):
        if plugin.get_name() in self.plugins:
            raise PluginAlreadyExist(plugin.get_name(), self.get_plugins_list())

        self.plugins[plugin.get_name()] = plugin
        event_engine = self.mediator.get_event_engine()
        event_engine.add_plugin(plugin.get_name, plugin.get_bindings())

    def get_plugins_list(self):
        list = []
        for plugin in self.plugins:
            list.append(plugin)

        return list