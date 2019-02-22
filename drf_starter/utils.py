import os

def get_required_env(key):
    result = os.getenv(key)
    if result is not None:
        return result
    raise KeyError('Required env var "%s" was not defined, cannot continue' % key)
