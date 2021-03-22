from random import randint


def encode_cipher(string):
    """Function to encode given string. Encoding is composed by following steps:
        1. All letters are replace by random letter
        2. Reverse list with characters
        3. Split by odd and even index and again replace by random letter (other shift for each list)
        4. Combination of two lists. Letters inserted alternately.
        5. Create a key based on previous activities
            5.1 Key contains two signs at the start 'oX' and random number (10-99). It is only
                for create key more complex and harder to decode.
            5.2 Replace order in key (example [aaabbb] => [bbbaaa])
    """

    characters = [chr(i) for i in range(32, 127)]  # getting characters from ASCII table
    characters.remove('/')  # at this moment causes bug in FastAPI

    # first step
    first_key = randint(10, len(characters) - 1)
    first_encode = []

    for letter in string:
        if characters.index(letter) + first_key > len(characters) - 1:
            index = characters.index(letter) + first_key - len(characters)
            first_encode.append(characters[index])
        else:
            first_encode.append(characters[characters.index(letter) + first_key])

    # second step
    list_reversed = first_encode[::-1]

    # third step
    even_index = [value for (index, value) in enumerate(list_reversed) if index % 2 == 0]
    odd_index = [value for (index, value) in enumerate(list_reversed) if index % 2 != 0]

    even_key = randint(1, len(characters) - 1)
    odd_key = randint(1, len(characters) - 1)

    if even_key == odd_key or len(str(even_key)) != len(str(odd_key)):
        while True:
            odd_key = randint(1, len(characters) - 1)
            if even_key != odd_key and len(str(even_key)) == len(str(odd_key)):
                break

    even_with_shift = []
    odd_with_shift = []

    for letter in even_index:
        if characters.index(letter) + even_key > len(characters) - 1:
            index = characters.index(letter) + even_key - len(characters)
            even_with_shift.append(characters[index])
        else:
            even_with_shift.append(characters[characters.index(letter) + even_key])

    for letter in odd_index:
        if characters.index(letter) + odd_key > len(characters) - 1:
            index = characters.index(letter) + odd_key - len(characters)
            odd_with_shift.append(characters[index])
        else:
            odd_with_shift.append(characters[characters.index(letter) + odd_key])

    # fourth step
    message_list = []

    for letter in even_with_shift:
        message_list.append(letter)

    index = 1
    for letter in odd_with_shift:
        message_list.insert(index, letter)
        index += 2

    encoded_message = ''.join(message_list)

    # fifth step (creating key)
    key = f'{first_key}{randint(10, 99)}{even_key}{odd_key}'

    user_key = [num for num in list(key)[::-1][3:]]
    user_key.extend(key[::-1][:3])

    secret_key = ''.join(user_key)

    return [encoded_message, f'oX{secret_key}']
