import string
import random
import clipboard


def do_letter(keys, letter):
    if letter == ' ':
        return keys['b'][random.randint(0, 5)]
    elif letter in string.lowercase:
        position = string.lowercase.index(letter)
        return keys['a'][position]
    else:
        return ' '


def do_sentence(keys, sentence):
    sentence = sentence.lower()
    encrypted = ''
    count = 0
    for char in sentence:
        should_enter_fabricated_char = random.randint(1, 10)
        if char == ' ':
            if count == 0:
                encrypted += keys['b'][random.randint(5, len(keys['b']) - 1)]
            else:
                count = 0
        encrypted += do_letter(keys, char)
        if should_enter_fabricated_char > 2:
            count += 1
            encrypted += keys['b'][random.randint(5, len(keys['b']) - 1)]
    return encrypted


def reorganize(sentence):
    encrypted = list(sentence)
    for i in range(0, len(sentence) - 1):
        if i % 2 == 0:
            saved = encrypted[i]
            encrypted[i] = encrypted[i+1]
            encrypted[i+1] = saved
    return ''.join(encrypted)


def do(keys, sentence):
    encrypted = do_sentence(keys, sentence)
    encrypted = reorganize(encrypted)
    clipboard.copy(encrypted)
    return encrypted
