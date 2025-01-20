def reverse(text):
    return text[:: -1]

def is_palindrome(text):
  return text == reverse(text)

something = input('ведите текст')
if (is_palindrome(something)):
  print('да, это палиндром')
else:
  print("нет это не палидром")
