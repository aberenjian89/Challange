def permutation(str):
    result = []
    helper("", str, result)
    return result


def helper(curr, str, result):
    if str == "":
        result.append(curr)

    i = 0
    while i < len(str):
        helper(curr+str[i], str[0:i]+str[i+1:], result)
        i += 1

    return result


print(permutation("Hello"))
