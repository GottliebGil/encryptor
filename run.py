import string
import random


def extract_key_from_file(file):
    count = {}
    current_key = open(file).readline()
    for char in current_key:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for option in count:
        if count[option] > 1:
            print "ERROR! %s appears more than one with %s occurrences in file %s" % (option, count[option], file)

    return current_key


def get_keys():
    key_a = extract_key_from_file('key_a.txt')
    key_b = extract_key_from_file('key_b.txt')
    return {
        'a': key_a,
        'b': key_b
    }


keys = get_keys()


def encrypt_letter(letter):
    position = string.lowercase.index(letter)
    return keys['a'][position]


def decrypt_letter(letter):
    position = keys['a'].index(letter)
    return string.lowercase[position]


def encrypt_replace_letters(sentence):
    sentence = sentence.lower()
    encrypted = ''
    for char in sentence:
        should_enter_fabricated_char = random.randint(1, 10)
        if char == ' ':
            encrypted += ' '
        else:
            encrypted += encrypt_letter(char)
        while should_enter_fabricated_char > 2:
            should_enter_fabricated_char = random.randint(1, 10)
            encrypted += keys['b'][random.randint(0, len(keys['b']) - 1)]
    return encrypted


def reorganize_letters(sentence):
    encrypted = list(sentence)
    for i in range(0, len(sentence)):
        if i % 2 == 0 and i < len(sentence) - 1:
            saved = encrypted[i]
            encrypted[i] = encrypted[i+1]
            encrypted[i+1] = saved
    return ''.join(encrypted)


def encrypt_sentence(sentence):
    encrypted = encrypt_replace_letters(sentence)
    encrypted = reorganize_letters(encrypted)
    return encrypted


def decrypt_replace_letters(sentence):
    decrypted = ''
    for char in sentence:
        if char == ' ':
            decrypted += ' '
        elif char in keys['a']:
            decrypted += decrypt_letter(char)
    return decrypted


def decrypt_sentence(sentence):
    decrypted = reorganize_letters(sentence)
    decrypted = decrypt_replace_letters(decrypted)
    return decrypted


enc = encrypt_sentence("Hi how are you")
print enc
print decrypt_sentence(enc)