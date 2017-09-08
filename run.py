import decrypt
import encrypt


def extract_key_from_file(file_name):
    count = {}
    current_key = open(file_name).readline()
    for char in current_key:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for option in count:
        if count[option] > 1:
            print "ERROR! %s appears more than one with %s occurrences in file %s" % (option, count[option], file_name)

    return current_key


def get_keys():
    key_a = extract_key_from_file('key_a.txt')
    key_b = extract_key_from_file('key_b.txt')
    return {
        'a': key_a,
        'b': key_b
    }


keys = get_keys()

enc = encrypt.do(keys, "Hi how are you")
print enc
print decrypt.do(keys, enc)