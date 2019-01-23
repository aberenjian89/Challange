def longest_substring(str):
    maximum = 0
    i = 0
    j = 0
    dic = {}
    while (j < len(str)):
        if str[j] not in dic:
            dic[str[j]] = True
            j += 1
            maximum = max([maximum, j-i])
        else:
            del dic[str[i]]
            i += 1
    return maximum


print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))
