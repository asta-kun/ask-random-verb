import json
from pydash.collections import reduce_ as reduce
from pydash.objects import keys

filenames = ('irregular', )

def get_verbs():
    """
    Readsfiles with verbs and returns a dict of them
    """
    verbs = {}
    
    for filename in filenames:
        with open('lib/core/verbs/%s.json' % filename, 'r') as f:
            data = json.load(f)
            verbs[filename] = data
            
            
    # join all the verbs
    verbs['all'] = reduce(keys(verbs), lambda state, key: state + verbs[key], [])
    
    return verbs