def encode(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError('number must be an integer')
    if number < 0:
        raise ValueError('number must be non-negative')

    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    base36 = ''

    if 0 <= number < len(alphabet):
        return alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return base36

def decode(number):
    return int(number, 36)