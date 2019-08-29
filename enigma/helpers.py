# -*- coding: utf-8 -*-


"""The helpers module"""


def alphabet_get():
    """The alphabet

    Returns: The latin upper alphabet A-Z as a string

    """
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def a0z25_encode(plain):
    """A0Z25 encoder

    Args:
        plain: String to encode

    Returns: Encoded string

    """
    plain = plain.encode()
    encoded = list()
    for b in plain:
        quotient = b
        c = ""
        while quotient > 0:
            c = alphabet_get()[quotient % 26] + c
            quotient = int(quotient / 26)
        encoded.append(c)
    encoded = "".join(encoded)
    return encoded


def a0z25_decode(encoded):
    """A0Z25 decoder

    Args:
        encoded: String to decode

    Returns: Decoded string

    """
    plain = bytearray()
    for i in range(0, len(encoded), 2):
        word = "".join(list(reversed(encoded[i:i + 2])))
        num = 0
        for power, car in enumerate(word):
            num += alphabet_get().find(car) * (26 ** power)
        plain.append(num)
    plain = plain.decode()
    return plain
