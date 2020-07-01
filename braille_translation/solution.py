BRAILLE_SYMBOLS_DOT_DICTIONARY = {
        'a': '1',
        'b': '12',
        'c': '14',
        'd': '145',
        'e': '15',
        'f': '124',
        'g': '1245',
        'h': '125',
        'i': '24',
        'j': '245',
        'k': '13',
        'l': '123',
        'm': '134',
        'n': '1345',
        'o': '135',
        'p': '1234',
        'q': '12345',
        'r': '1235',
        's': '234',
        't': '2345',
        'u': '136',
        'v': '1236',
        'w': '2456',
        'x': '1346',
        'y': '13456',
        'z': '1356',
        '1': '1',
        '2': '12',
        '3': '14',
        '4': '145',
        '5': '15',
        '6': '124',
        '7': '1245',
        '8': '125',
        '9': '24',
        '0': '245',
        ',': '2',
        ';': '23',
        ':': '25',
        '.': '256',
        '?': '236',
        '!': '235',
        '\'': '3',
        '-': '36',
        ' ': ''
        }
BRAILLE_INDICATOR_DOTS_DICTIONARY = {
        'capital': '6',
        'number': '3456'
        }

def get_dot_numbers_of(character):
    return BRAILLE_SYMBOLS_DOT_DICTIONARY[character.lower()]

def convert_to_binary_string_from(dot_numbers):
    binary_string = '000000'

    for each_number in dot_numbers:
        dot_number = int(each_number)
        dot_cell_index = dot_number - 1
        binary_string = binary_string[:dot_cell_index] + '1' + binary_string[dot_cell_index + 1:]

    return binary_string

def get_indicator_dot_numbers_of(character):
    if character.isupper():
        return BRAILLE_INDICATOR_DOTS_DICTIONARY['capital']
    elif character.isdigit():
        return BRAILLE_INDICATOR_DOTS_DICTIONARY['number']
    else:
        return None

def get_binary_string_of(character):
    binary_string = ''
    indicator_dot_numbers = get_indicator_dot_numbers_of(character)

    if indicator_dot_numbers is not None:
        binary_string = convert_to_binary_string_from(indicator_dot_numbers) + binary_string

    dot_numbers = get_dot_numbers_of(character)
    binary_string += convert_to_binary_string_from(dot_numbers)

    return binary_string

def solution(text):
    text_binary_string = ''

    for each_character in text:
        text_binary_string += get_binary_string_of(each_character)

    return text_binary_string

assert solution('code') == '100100101010100110100010'
assert solution('Braille') == '000001110000111010100000010100111000111000100010'
assert solution('The quick brown fox jumps over the lazy dog') == '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'
