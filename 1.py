def min(source, target):
    len_1 = len(source)
    len_2 = len(target)
    i, j, count = 0, 0, 0
    while j < len_2:
        i = 0
        ans = False
        while i < len_1 and j < len_2:
            if source[i] == target[j]:
                j = j + 1
                ans = True
            i = i + 1
        if not ans:
            return -1
        count = count + 1
    return count


print(min("abc", "abcbc"))
print(min("abc", "acdbc"))
print(min("xyz", "xzyxz"))
