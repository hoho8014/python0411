# function1.py
#함수를 정의
def setValue(i):
        x = i
        print("내부에서 출력:", x)

#함수를 호출
retValue = setValue(5)
print(retValue)

#함수를 정의
def swap(x,y):
    return y,x

#호출
print(swap(2,3))
