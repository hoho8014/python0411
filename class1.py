# class1.py
#클래스정의(형식)
class person:
    #클래스의 멤버변수(주로 데이터를 공유)
    num_person = 0
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
    #인스턴스 메서드
    def print(self):
        print("my nams is {0}".format(self.name))

#인스턴스 생성
p1 = person()
p2 = person()
p2.name = "전우치"
p1.print()
p2.print()