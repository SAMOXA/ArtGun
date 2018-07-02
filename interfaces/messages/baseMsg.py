class BaseMsgError(Exception):
    pass


class BaseMsgFieldNotExist(BaseMsgError):
    field = ''
    msgDump = {}

    def __init__(self, field, msg_dump = None):
        self.field = field
        self.msgDump = msg_dump


class BaseMsg:
    fields = dict()
    base_version_fields = dict()
    base_version_fields['0.1'] = ['source', 'destination', 'tag', 'sync', 'one_shot', 'version', 'base_version']
    version_fields = dict()

    def __init__(self, source='', dest='', tag=-1, version='0.0', sync=True, one_shot=False):
        self.fields['source'] = source
        self.fields['destination'] = dest
        self.fields['tag'] = tag
        self.fields['sync'] = sync
        self.fields['one_shot'] = one_shot
        self.fields['version'] = version
        self.fields['base_version'] = '0.1'

    def get_fields_list(self):
        return self.fields.keys()

    def get_field(self, field):
        if field not in self.fields:
            raise BaseMsgFieldNotExist(field, self.fields)

        return self.fields[field]

    def set_field(self, field, value):
        if field not in self.fields:
            raise BaseMsgFieldNotExist(field, self.fields)

        self.fields = value

    def get_base_version(self):
        return self.fields['base_version']

    def get_base_version_fields(self, version='0.1'):
        return self.base_version_fields[version]

    def get_version(self):
        return self.fields['version']

    def get_version_fields(self, version=''):
        return self.version_fields[version]

    def turn_back(self):
        dest = self.fields['destination']
        self.fields['destination'] = self.fields['source']
        self.fields['source'] = dest

    def clone(self):
        msg = BaseMsg()
        msg.fields = self.fields
        return msg
