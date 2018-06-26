from unittest import TestCase
from plugins.saveBooru.safeBooru import SaveBooruPlugin


class TestPluginSaveBooru(TestCase):
    def test_plugin_saveBooru_get_id(self):
        plugin = SaveBooruPlugin()
        params = {
            "id": 2392469
        }
        plugin.get_by_id(params)
        del plugin

    def test_plugin_saveBooru_get_id_multiple(self):
        plugin = SaveBooruPlugin()
        params = {
            "id": 2392469
        }
        plugin.get_by_id(params)
        plugin.get_by_id(params)
        plugin.get_by_id(params)
        plugin.get_by_id(params)
        plugin.get_by_id(params)
        del plugin

    def test_plugin_saveBooru_get_tag(self):
        plugin = SaveBooruPlugin()
        params = {
            "tags": ["cat"],
        }
        plugin.get_by_tags(params)
        del plugin

    def test_plugin_saveBooru_get_tag_mult(self):
        plugin = SaveBooruPlugin()
        params = {
            "tags": ["cat", "girl"],
        }
        plugin.get_by_tags(params)
        del plugin