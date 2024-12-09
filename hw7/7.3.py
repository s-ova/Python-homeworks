def second_index(text, some_str):
    found_count = 0
    for i in range(len(text)):
        if text[i:i+len(some_str)] == some_str:
            found_count += 1
            if found_count == 2:
                return i
    return None
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')