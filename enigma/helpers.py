# -*- coding: utf-8 -*-


"""The helpers module"""

from collections import namedtuple


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


def internals_settings():
    return {
               "etw": {
                   "in": alphabet(),
                   "out": alphabet(),
               },
               "i": {
                   "in": alphabet(),
                   "out": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
               },
               "ii": {
                   "in": alphabet(),
                   "out": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
               },
               "iii": {
                   "in": alphabet(),
                   "out": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
               },
               "iv": {
                   "in": alphabet(),
                   "out": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
               },
               "v": {
                   "in": alphabet(),
                   "out": "VZBRGITYUPSDNHLXAWMJQOFECK",
               },
               "vi": {
                   "in": alphabet(),
                   "out": "JPGVOUMFYQBENHZRDKASXLICTW",
               },
               "vii": {
                   "in": alphabet(),
                   "out": "NZJHGRCXMYSWBOUFAIVLPEKQDT",
               },
               "viii": {
                   "in": alphabet(),
                   "out": "FKQHTLXOCBJSPDZRAMEWNIUYGV",
               },
               "beta": {
                   "in": alphabet(),
                   "out": "LEYJVCNIXWPBQMDRTAKZGFUHOS",
               },
               "gamma": {
                   "in": alphabet(),
                   "out": "FSOKANUERHMBTIYCWLQPZXVGJD",
               },
               "ukw-b": {
                   "in": alphabet(),
                   "out": "ENKQAUYWJICOPBLMDXZVFTHRGS",
               },
               "ukw-c": {
                   "in": alphabet(),
                   "out": "RDOBJNTKVEHMLFCWZAXGYIPSUQ",
               },
           },
