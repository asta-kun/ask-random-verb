import sys, re

remove = [
    re.compile('(.*)\.py$'),
    re.compile('^--'),
    re.compile('^-'),
    ]

def remove_fn(name):
    raw = name.strip()
    for r in remove:
        raw = r.sub('', raw)
    return raw

def get_arguments():
    args = [remove_fn(arg) for arg in sys.argv]
    return list(filter(lambda i: len(i) > 0, args))

