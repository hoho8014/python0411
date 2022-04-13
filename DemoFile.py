# DemoFile.py
#문자열을 결합 연산
url = "http://www.credu.com/?page=" + str(1)
print(url)

#정렬방식 지정
for x in range(1,6):
    print(x,"*",x,"=",x*x)


print("---약간 수정---")
for x in range(1,6):
    print(x,"*",x,"=",x*x,str(x*x).rjust(3))

print("---약간 수정---")
for x in range(1,6):
    print(x,"*",x,"=",x*x,str(x*x).zfill(5))

#서식문자 지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

#파일을 쓰기(파이썬은 태생이 리눅스, 유닉스)
f = open("c:\\work\\demo.txt","wt")
#약간불편(오래된 언어)
f.write("한글데이터\nabcd\n1234\n")
f.close()

