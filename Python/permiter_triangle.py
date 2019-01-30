def triangle_permiter(a):
    a.sort()
    max_p = 0
    i = 0
    while i < len(a):
        j = i + 1
        while j < len(a):
            if j + 1 < len(a):
                if a[i] + a[j+1] > a[j] and a[j]+a[j+1] > a[i] and a[i]+a[j] > a[j+1]:
                    res = a[i]+a[j]+a[j+1]
                    max_p = max(max_p, res)
            j += 1
        i += 1
    return max_p


print(triangle_permiter([2, 1, 2]))
print(triangle_permiter([1, 2, 1]))
print(triangle_permiter([3, 2, 3, 4]))
print(triangle_permiter([3, 6, 2, 3]))
