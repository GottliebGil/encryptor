import string


def do_letter(keys, letter):
    if letter in keys['a']:
        position = keys['a'].index(letter)
        return string.lowercase[position]
    else:
        return ' '


def reorganize(sentence):
    encrypted = list(sentence)
    for i in range(0, len(sentence)):
        if i % 2 == 0 and i < len(sentence) - 1:
            saved = encrypted[i]
            encrypted[i] = encrypted[i+1]
            encrypted[i+1] = saved
    return ''.join(encrypted)


def do_sentence(keys, sentence):
    decrypted = ''
    for char in sentence:
        if char == ' ':
            decrypted += ' '
        elif char in keys['a']:
            decrypted += do_letter(keys, char)
    return decrypted


def do(keys, sentence):
    decrypted = reorganize(sentence)
    decrypted = do_sentence(keys, decrypted)
    return decrypted
