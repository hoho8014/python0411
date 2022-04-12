# class1.py
#클래스정의(형식)
class person:
    #클래스의 멤버변수(주로 데이터를 공유)
    num_person = 0
    #초기화 메서드
    def __init__(self):
        #인스턴스 멤버변수(복사본에 해당)
        self.name = "default name"
        person.num_person += 1
    #인스턴스 메서드
    def print(self):
        print("my nams is {0}".format(self.name))

#인스턴스 생성
p1 = person()
p2 = person()
p3 = person()

print("인스턴스 개수:", person.num_person)

#클래스에 추가
person.title = "new title"
print(person.title)
print(p1.title)
#인스턴스에 추가
p1.age = 30
print(p1.age)
#print(p2.age)

