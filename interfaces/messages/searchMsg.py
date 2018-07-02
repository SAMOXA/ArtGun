from interfaces.messages.baseMsg import BaseMsg


class SearchMsg(BaseMsg):

    def __init__(self, source='', dest='', tag=-1, sync=True, one_shot=False):
        BaseMsg.__init__(self, source, dest, tag, '0.1', sync, one_shot)
        BaseMsg.version_fields['0.1'] = ['type', 'id', 'tags']

        BaseMsg.fields['type'] = 'None'
        BaseMsg.fields['id'] = ''
        BaseMsg.fields['tags'] = []