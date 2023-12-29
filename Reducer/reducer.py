
def main(shuffled):
    result = {}
    for key in shuffled:
        values = shuffled[key]
        total = 0
        for number in values:
            total += number
        result[key] = total
    return result
