
def _get_redis_events():
    return []


def _get_impacted_collections(events):
    return []


def _poke_balrog(collection_ids):
    pass


def main():
    # 1. grab things in the redis list
    events = _get_redis_events()

    # 2. combine per-collection
    collection_ids = _get_impacted_collections(events)

    # 3. send it to Balrog
    _poke_balrog(collection_ids)
