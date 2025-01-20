from itertools import starmap

def composition(*x):
    # произведение
    for n, i in enumerate(x):
        if n==0:
            rez = i
        else:
            rez = rez * i
    return rez 

# произведение
x = starmap(composition, [(2,5,3), (3,2,1), (10,10,3)])
list(x)
# [30, 6, 300]

# квадраты
x = starmap(pow, [(2,5), (3,2), (10,3)])
list(x)
# [32, 9, 1000]

# max
x = starmap(max, [(2,5,4), (3,2,1), (10,3,8)])
list(x)
# [5, 3, 10]

# min
x = starmap(min, [(2,5,9,3), (3,2,6,8), (1,0,10,3)])
list(x)
# [2, 2, 3]
