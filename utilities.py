def read_file(name):
    with open (name) as f:
        lines = f.readlines()
        f.close()
    return lines

def remove_comments(line):
    idx = line.find("//")
    return line[0:idx]

def remove_whitespace(line):
    whitespaces = ['\n', '\t']
    for el in whitespaces:
        if el in line:
            line = line.replace(el, '')
    return line
