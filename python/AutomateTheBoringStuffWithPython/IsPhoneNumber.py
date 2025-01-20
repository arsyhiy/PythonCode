def IsPhoneNumber(number):
    
    if len(number) != 12:
        return False
    for i in range(0, 3):
        if not number[i].isdecimal():
            return False
    if number[3] != '-':
        return False
    for i in range(4, 7):
        if not number[i].isdecimal():
            return False
    if number[7] != '-':
        return False
    for i in range(8, 12):
        if not number[i].isdecimal():
            return False
    return True

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
    chunk = message[i:i+12]
    if IsPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# reason why so many if, for statements because i don't know  the beter solutions for this