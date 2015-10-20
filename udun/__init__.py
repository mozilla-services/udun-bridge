import sys
import argparse
import os


_here = os.path.dirname(__file__)
DEFAULT_CONF = os.path.join(_here, '..', 'conf', 'udun.ini')
__version__ = '0.1'


def _read_args(args=None):
    parser = argparse.ArgumentParser(description='Udun.')

    parser.add_argument('--version', action='store_true', default=False,
                        help='Displays version and exits.')

    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help='Verbose')

    parser.add_argument('-c', '--config', help='config file',
                        type=str, default=DEFAULT_CONF)

    return parser.parse_args(args=args)


def _get_redis_events(host, port, listname):
    import redis
    server = redis.StrictRedis(host=host, port=port, db=0)

    # 1. read the size of the list with llen
    size = server.llen(listname)

    # 2. get llen elements (it's ok if we get more added while doing it)
    for i in range(size):
        yield server.lpop(listname)


def _get_impacted_collections(events):
    collections = []
    for event in events:
        collection_id = event.get('collection_id')
        if collection_id and collection_id not in collections:
            collections.append(collection_id)
            yield collection_id


def _poke_balrog(collection_ids):
    for collection_id in collection_ids:
        # generate one PUT per collection_id
        pass


def main(args=None):
    # 1. read the command-line options
    args = _read_args(args)

    if args.version:
        print(__version__)
        sys.exit(0)

    # 2. grab the config
    from konfig import Config
    config = Config(args.config).get_map('udun')

    # 3. grab things in the redis list
    events = _get_redis_events(config.get('redis_host', 'localhost'),
                               config.get('redis_port', 6379),
                               config.get('redis_listname', 'udun'))

    # 4. combine per-collection
    collection_ids = _get_impacted_collections(events)

    # 5. send it to Balrog
    _poke_balrog(collection_ids)
