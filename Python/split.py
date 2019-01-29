def split(s, delimiter):
    result = []
    str = ""
    length = len(delimiter)
    i = 0
    while i < len(s):
        if s[i:i+length] == delimiter:
            result.append(str)
            i = i + length
            str = ''
        else:
            str += s[i]
            i += 1

    if str != '':
        result.append(str)

    return result


print(split("edededcabd", "ed"))
