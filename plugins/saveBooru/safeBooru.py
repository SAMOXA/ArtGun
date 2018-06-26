import requests
import json
import logging
from libs.ThreadedQueueWorker.threadedQueueWorker import ThreadedQueueWorker

MAX_LIMIT = 1000
URL_ID = 'http://safebooru.org/index.php?page=dapi&s=post&json=1&q=index&id={0}'
URL_TAGS = 'http://safebooru.org/index.php?page=dapi&s=post&json=1&q=index&limit={2}&tags={0}&pid={1}'


def __make_request(url):
    with requests.session() as s:
        with s.get(url) as response:
            return response.text


def convert_from_savebooru_api(arts):
    converted = []
    for ids in arts:
        url = "https://safebooru.org/images/{0}/{1}".format(ids['directory'], ids['image'])
        thumb_url = "https://safebooru.org/thumbnails/{0}/thumbnail_{1}".format(ids['directory'], ids['image'])
        converted.append({
            "id": ids['id'],
            "hash": ids['hash'],
            "url": url,
            "thum_url": thumb_url,
            "width": ids['width'],
            "height": ids['height'],
            "author": ids['owner'],
            "tags": ids['tags']
        })

    return converted


def request_worker_thread(req):
    if req["type"] == "by_id":
        resp = __make_request(URL_ID.format(req["id"]))
        return resp

    if req['type'] == "by_tags":
        req_tags = ""
        for tag in req['tags']:
            req_tags += tag + "+"
        req_tags = req_tags[:-1]
        resp = __make_request(URL_TAGS.format(req_tags, str(req["page"]), str(req["limit"])))
        return resp


def response_worker_thread(resp):
    art = json.loads(resp)
    print(convert_from_savebooru_api(art))


class SaveBooruPlugin(ThreadedQueueWorker):
    default_limit = 10

    def __init__(self):
        ThreadedQueueWorker.__init__(self, request_worker_thread, response_worker_thread)
        self.start_threads()

    def __del__(self):
        self.stop_threads()

    def get_by_id(self, props):
        params = dict()
        params['id'] = props["id"]
        params['type'] = "by_id"
        self.push(params)

    def get_by_tags(self, props):
        params = dict()
        params['tags'] = props["tags"]
        params['page'] = 0
        if 'page' in props:
            params['page'] = props["page"]

        params['limit'] = 5
        if 'limit' in props:
            params['limit'] = props["limit"]

        params['type'] = "by_tags"
        self.push(params)
