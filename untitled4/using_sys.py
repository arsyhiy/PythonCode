import sys

print("Аргументы командной строки:")
for i in sys.argv:
    print(i)
print('\n\nпеременная pythonpath содержит', sys.path, '\n')