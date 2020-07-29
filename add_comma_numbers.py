def add_comma(number):
    if isinstance(number, str) != True:
        number = str(number)

    i = 3

    while i < len(number):
        pos = -i
        number = number[:pos] + ',' + number[pos:]
        i += 4

    return number
