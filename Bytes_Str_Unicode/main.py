
'''
   python 3 code below
'''

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str, str):
    if isinstance(bytes_or_str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value


'''
   python 2 code below
'''


def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode("utf-8")
    else:
        value = unicode_or_str
    return value
