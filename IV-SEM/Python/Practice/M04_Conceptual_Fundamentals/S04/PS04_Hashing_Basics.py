def frequency_count(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
print(frequency_count("aabbcc"))