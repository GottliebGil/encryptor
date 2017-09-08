import string
import random


def generate_key(keys):
    val = string.printable.rstrip()
    val = [x for x in val if x not in keys['a'] and x not in keys['b']]
    val = ''.join(val)
    secure_random = random.SystemRandom()
    if len(keys['a']) > 0:
        key = val
    else:
        key = secure_random.sample(val, 26)
    key = ''.join(key)
    return key


def do():
    keys = {
        'a': [],
        'b': []
    }
    keys['a'] = generate_key(keys)
    keys['b'] = generate_key(keys)
    open('key_a.txt', 'w').write(keys['a'])
    open('key_b.txt', 'w').write(keys['b'])
    print "a: %s" % keys['a']
    print "b: %s" % keys['b']
    return keys