
def main(keyValue):
    key, value = keyValue
    words = value.split()
    result = {word: 1 for word in words}
    return result
