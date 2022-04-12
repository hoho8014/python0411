# function2.py
#전역변수
x = 1
def func(a):
    return x+a

#호출
print(func(1))

def func(a):
    #지역변수
    x = 2
    return x+a
    
#호출
print(func 2(1))

#불변형식
a = 1.2
print(id(a))
a = 2.3
print(id(a))
