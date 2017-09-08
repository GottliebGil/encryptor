import string
import random
import os


def generate_key(keys):
    val = [x for x in string.printable.rstrip()]
    random.shuffle(val)
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
    if os.path.exists('key_a.txt') and os.path.exists('key_b.txt'):
        new_dir_path = 'old_keys/%s' % os.path.getctime('key_a.txt')
        os.makedirs(new_dir_path)
        os.rename('key_a.txt', "%s/key_a.txt" % new_dir_path)
        os.rename('key_b.txt', "%s/key_b.txt" % new_dir_path)

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
