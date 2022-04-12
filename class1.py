# class1.py
#클래스정의(형식)
class person:
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
    #인스턴스 메서드
    def print(self):
        print("my nams is {0}".format(self.name))

#인스턴스 생성