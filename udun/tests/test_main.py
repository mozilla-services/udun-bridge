import json
import unittest
from udun import main
import redis


class MainTest(unittest.TestCase):
    def test_main(self):
        # fill redis with some stuff
        server = redis.StrictRedis(host='localhost', port=6379, db=0)
        for collection in ('1', '2', '3'):
            rec = {'collection_id': collection}
            server.lpush('udun', json.dumps(rec))

        args = []
        main(args)

    def test_version(self):

        args = ['--version']
        try:
            main(args)
        except SystemExit:
            pass
