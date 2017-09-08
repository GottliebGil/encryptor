import string
import random


def do_letter(keys, letter):
    position = string.lowercase.index(letter)
    return keys['a'][position]


def do_sentence(keys, sentence):
    sentence = sentence.lower()
    encrypted = ''
    count = 0
    for char in sentence:
        should_enter_fabricated_char = random.randint(1, 10)
        if char == ' ':
            if count == 0:
                encrypted += keys['b'][random.randint(0, len(keys['b']) - 1)]
            else:
                count = 0
            encrypted += ' '
        else:
            encrypted += do_letter(keys, char)
        if should_enter_fabricated_char > 2:
            count += 1
            should_enter_fabricated_char = random.randint(1, 10)
            encrypted += keys['b'][random.randint(0, len(keys['b']) - 1)]
    return encrypted


def reorganize(sentence):
    encrypted = list(sentence)
    for i in range(0, len(sentence)):
        if i % 2 == 0 and i < len(sentence) - 1:
            saved = encrypted[i]
            encrypted[i] = encrypted[i+1]
            encrypted[i+1] = saved
    return ''.join(encrypted)


def do(keys, sentence):
    encrypted = do_sentence(keys, sentence)
    encrypted = reorganize(encrypted)
    return encrypted
