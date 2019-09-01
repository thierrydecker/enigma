# -*- coding: utf-8 -*-

"""The tools module

"""


def alphabet():
    """The alphabet

    Returns: The latin upper alphabet A-Z as a string

    """
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def a0z25_encode(plain, codec="utf8"):
    """A0Z25 encoder

    Args:
        plain: String to encode
        codec: Codec of the string to encode

    Returns: Encoded string

    """
    plain = plain.encode(encoding=codec)
    encoded = list()
    for b in plain:
        quotient = b
        c = ""
        while quotient > 0:
            c = alphabet()[quotient % 26] + c
            quotient = int(quotient / 26)
        encoded.append(c)
    encoded = "".join(encoded)
    return encoded


def a0z25_decode(encoded, codec="utf8"):
    """A0Z25 decoder

    Args:
        encoded: String to decode
        codec: Codec of the decoded string

    Returns: Decoded string

    """
    plain = bytearray()
    for i in range(0, len(encoded), 2):
        word = "".join(list(reversed(encoded[i:i + 2])))
        num = 0
        for power, car in enumerate(word):
            num += alphabet().find(car) * (26 ** power)
        plain.append(num)
    plain = plain.decode(encoding=codec)
    return plain


def wheels_wirings():
    """The wheels wirings

    Returns: The initial wheels wirings known from historical documents

    """
    return {
        "etw": {
            "in": alphabet(),
            "out": alphabet(),
            "turn_over": "",
        },
        #
        # Standard wheels
        #
        "i": {
            "in": alphabet(),
            "out": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "turn_over": "Q",
        },
        "ii": {
            "in": alphabet(),
            "out": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "turn_over": "E",
        },
        "iii": {
            "in": alphabet(),
            "out": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
            "turn_over": "V",
        },
        "iv": {
            "in": alphabet(),
            "out": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
            "turn_over": "J",
        },
        "v": {
            "in": alphabet(),
            "out": "VZBRGITYUPSDNHLXAWMJQOFECK",
            "turn_over": "Z",
        },
        #
        # Extra wheels VI-VIII
        #
        "vi": {
            "in": alphabet(),
            "out": "JPGVOUMFYQBENHZRDKASXLICTW",
            "turn_over": "ZM",
        },
        "vii": {
            "in": alphabet(),
            "out": "NZJHGRCXMYSWBOUFAIVLPEKQDT",
            "turn_over": "ZM",
        },
        "viii": {
            "in": alphabet(),
            "out": "FKQHTLXOCBJSPDZRAMEWNIUYGV",
            "turn_over": "ZM",
        },
        #
        # Fourth "thin" wheel also called "greek wheel"
        # Zusatzwalze Beta (β) and Gamma (γ)
        #
        "beta": {
            "in": alphabet(),
            "out": "LEYJVCNIXWPBQMDRTAKZGFUHOS",
            "turn_over": "",
        },
        "gamma": {
            "in": alphabet(),
            "out": "FSOKANUERHMBTIYCWLQPZXVGJD",
            "turn_over": "",
        },
        #
        # Reflectors
        #
        "ukw-b": {
            "in": alphabet(),
            "out": "ENKQAUYWJICOPBLMDXZVFTHRGS",
            "turn_over": "",
        },
        "ukw-c": {
            "in": alphabet(),
            "out": "RDOBJNTKVEHMLFCWZAXGYIPSUQ",
            "turn_over": "",
        },
    }
