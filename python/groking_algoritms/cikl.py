# def countdown():
#   print (3,2,1)
#
# countdown()

def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)

countdown(3)

def greet(name):
    print("hello," + name + "!")
    greet2(name)
    print("getting ready to say byy...")
    bye()

def greet2(name):
    print("how are you," + name + "?")

def bye():
    print("ok bye!")

greet("magie")


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(5))#=5*4*3*2*1