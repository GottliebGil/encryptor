import string


def get_key():
    count = {}
    line = open('key.txt').readline()
    for char in line:
        if count.has_key(char):
            count[char] += 1
        else:
            count[char] = 1

    for option in count:
        if count[option] > 1:
            print "ERROR! %s appears more than one with %s occurrences" % (option, count[option])

    return line


key = get_key()


def encrypt_letter(letter):
    position = string.lowercase.index(letter)
    return key[position]


def decrypt_letter(letter):
    position = key.index(letter)
    return string.lowercase[position]


def encrypt_sentence(sentence):
    sentence = sentence.lower()
    encrypted = ''
    for char in sentence:
        if char == ' ':
            encrypted += ' '
        else:
            encrypted += encrypt_letter(char)
    return encrypted


def decrypt_sentence(sentence):
    decrypted = ''
    for char in sentence:
        if char == ' ':
            decrypted += ' '
        else:
            decrypted += decrypt_letter(char)
    return decrypted


enc = encrypt_sentence("Hi how are you")
print enc
print decrypt_sentence(enc)