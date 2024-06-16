def b36encode(number):
    if not isinstance(number, (int, float)):
        raise ValueError("must supply an integer or float")
    if number < 0:
        raise ValueError("must supply a non-negative number")
    number = int(number)
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    base36 = ''
    while number != 0:
        number, i = divmod(number, 36)
        base36 = alphabet[i] + base36
    return base36 or alphabet[0]

def b36decode(number):
    return int(number, 36)