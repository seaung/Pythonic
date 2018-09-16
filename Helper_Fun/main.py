from urllib.parse import parse_qs


my_values = parse_qs('red=3&blue=0&green=', keep_blank_value=True)

print(my_values)

print('red', my_values.get('red'))

print(my_values.get('red')[0], or 0)

print(int(my_values.get('red', [''])[0] or 0))


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found
