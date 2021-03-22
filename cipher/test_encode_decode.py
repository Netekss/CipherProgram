import pytest
import random

from encode import encode_cipher
from decode import decode_cipher


def test():
    """Testing if function encode_cipher and decode_cipher works fine"""

    characters = [chr(i) for i in range(32, 127)]
    characters.remove('/')
    testing_sting = ''

    for i in range(1, 50):
        testing_sting += random.choice(characters)

    encoded_message = encode_cipher(testing_sting)
    decoded_message = decode_cipher(encoded_message[0], encoded_message[1])

    assert testing_sting == decoded_message
