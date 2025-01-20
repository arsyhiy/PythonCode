import re

tests = ["Something to match", "Second one is present"]
pattern1 = r"^.*(thing).*"
pattern2 = r"^.*(present).*"

# код без использования оператора `walrus`
for test in tests:
    m = re.match(pattern1, test)
    if m:
        print(f"Совпало с 1-м образцом: {m.group(1)}")
    else:
        m = re.match(pattern2, test)
        if m:
            print(f"Совпало с 2-м образцом: {m.group(1)}")

# Вывод
# Совпало с 1-м образцом: 'thing'
# Совпало с 2-м образцом: 'present'


# эквивалентный код с использованием
# оператора `walrus`
for test in tests:
    if m := (re.match(pattern1, test) or re.match(pattern2, test)):
        print(f"Matched: '{m.group(1)}'")

# Вывод
# Подходит: 'thing'
# Подходит: 'present'
