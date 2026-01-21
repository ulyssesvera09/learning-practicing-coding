def parse_inline_code(sentence):
    ind_list = list(sentence)
    indices = []

    for i, ch in enumerate(ind_list):
        if ch == '`':
            indices.append(i)
          
# list should contain odd and even numbers
# odd = <code> even = </code>

    for i, index in enumerate(indices):
        if i%2 == 0:
            sentence = sentence.replace('`', '<code>', 1)
        else:
            sentence = sentence.replace('`', '</code>', 1)
    return sentence
