import decrypt
import encrypt
import os
import generate_keys


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
    if os.path.exists('key_a.txt') and os.path.exists('key_b.txt'):
        key_a = extract_key_from_file('key_a.txt')
        key_b = extract_key_from_file('key_b.txt')
        return {
            'a': key_a,
            'b': key_b
        }
    else:
        return {
            'a': [],
            'b': []
        }


def print_menu():
    os.system('clear')
    print "Welcome to the ENCRYPTOR. Select what you wish to do:"
    print "1. Encrypt sentence"
    print "2. Decrypt sentence"
    print "3. Generate new keys"
    print "E. Quit program"


def print_need_to_generate_keys(keys):
    os.system('clear')
    print "WELCOME TO THE ENCRYPTOR. The software couldn't find any existing keys. Therefore, it will generate new ones."
    raw_input("Press ENTER to generate new keys")
    keys = generate_keys.do()
    raw_input("Keys were generated. Press ENTER to continue")


def main(keys):
    if len(keys['a']) == 0:
        print_need_to_generate_keys(keys)
    print_menu()
    selection = raw_input()
    while selection != 'E':
        os.system('clear')
        if selection == '1':
            print ' --- ENCRYPTION ---'
            print 'Use only English alphabet without special characters'
            enc = encrypt.do(keys, raw_input("Enter your sentence: "))
            print "Sentence was encrypted and copied into your clipboard: %s" % enc
        elif selection == '2':
            print ' --- DECRYPTION ---'
            dec = decrypt.do(keys, raw_input("Enter your sentence: "))
            print "It means: '%s'" % dec
        elif selection == '3':
            print ' --- GENERATE NEW KEYS ---'
            keys = generate_keys.do()
            print "Keys were generated and saved. Please keep them safe"
        else:
            print 'You have entered \'%s\'. This option doesn\'t exist.' % selection
        raw_input("Press ENTER to continue")
        print_menu()
        selection = raw_input()


main(get_keys())