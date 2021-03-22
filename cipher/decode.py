def decode_cipher(string, key):
    """Function to decode given string. Decoding is composed by following steps:
        1. Check length of key, decode true value of a key and split giver string by odd and even index.
            1.1 Skip first two characters
            1.2 Get correct order
            1.3 Get shifts from key for letters on even and odd index
        2. Decode letters on even and odd index by their key.
        3. Create list with letters in correct order.
            3.1 Add letter with even index, next add letters with odd index starts on 1 place and step 2
        4. Reverse list.
        5. Decode received list of letters by their common key.
    """

    # first step
    if len(key) == 8:
        user_key = key[2:]
        true_key = (user_key[3:] + user_key[:3])[::-1]

        even_index = [letter for letter in string[0::2]]
        odd_index = [letter for letter in string[1::2]]

        shift_even = int(true_key[-2]) * -1
        shift_odd = int(true_key[-1]) * -1

    elif len(key) == 10:
        user_key = key[2:]
        true_key = (user_key[5:] + user_key[:5])[::-1]

        even_index = [letter for letter in string[0::2]]
        odd_index = [letter for letter in string[1::2]]

        shift_even = int(true_key[4:6]) * -1
        shift_odd = int(true_key[-2:]) * -1

    else:
        return 'Incorrect key'

    characters = [chr(i) for i in range(32, 127)]  # getting characters from ASCII table
    characters.remove('/')  # at this moment causes bug in FastAPI

    # second step
    first_decode = [[], []]

    for letter in even_index:
        index = shift_even
        first_decode[0].append(characters[characters.index(letter) + index])

    for letter in odd_index:
        index = shift_odd
        first_decode[1].append(characters[characters.index(letter) + index])

    # third step
    second_decode = []

    for letter in first_decode[0]:
        second_decode.append(letter)

    index = 1
    for letter in first_decode[1]:
        second_decode.insert(index, letter)
        index += 2

    # fourth step
    list_reversed = second_decode[::-1]

    # fifth step
    value_to_return = []

    for letter in list_reversed:
        index = int(true_key[0:2]) * -1
        value_to_return.append(characters[characters.index(letter) + index])

    return ''.join(value_to_return)
