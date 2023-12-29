
def main(mapped):
    result = {}
    for mapped_output in mapped:
        for word in mapped_output:
            value = mapped_output[word]
            if word in result:
                result[word].append(value)
            else:
                result[word] = [value]
    return result
