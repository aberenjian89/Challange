def rollTheString(s, roll):
    # Write your code here
    roll.sort(reverse=True)
    i = 0
    alph = 'abcdefghijklmnopqrstuvwxyz'
    new_str = ''
    while i < len(roll):
        res = roll[i]
        new_str += alph[alph.index(s[i]) + res]
        i += 1
    return new_str


print(rollTheString('ccz', [3, 2, 1]))
