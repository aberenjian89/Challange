def strwithout3a3b(a, b):
    length = a + b
    str = ""
    i = 0
    count_a = 0
    count_b = 0
    while i < length:
        if a >= b:
            if a > 0 and count_a+1 < 3:
                str += 'a'
                count_a += 1
                count_b = 0
                a -= 1
            else:
                count_a = 0
                if b > 0 and count_b+1 < 3:
                    str += 'b'
                    count_b += 1
                    b -= 1
        else:
            if b > 0 and count_b+1 < 3:
                str += 'b'
                count_b += 1
                count_a = 0
                b -= 1
            else:
                count_b = 0
                if a > 0 and count_a+1 < 3:
                    str += 'a'
                    count_a += 1
        i += 1
    print(str)
    return str


strwithout3a3b(4, 5)
