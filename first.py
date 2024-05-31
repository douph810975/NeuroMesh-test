def count_subsequences(source, target):
    # 检查target中的字符是不是都在source中
    unique_chars_source = set(source)
    for char in target:
        if char not in unique_chars_source:
            return -1
    
    subsequences_count = 0
    i = 0  # target的index
    
    while i < len(target):
        subsequences_count += 1
        j = 0  # source index
        while i < len(target) and j < len(source):
            if target[i] == source[j]:
                i += 1
            j += 1
    
    return subsequences_count

print(count_subsequences("abc", "abcbc"))  
print(count_subsequences("abc", "acdbc"))  
print(count_subsequences("xyz", "xzyxz")) 