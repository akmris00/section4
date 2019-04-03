#리스트 자료형(순서, 중복, 수정, 삭제 모두 가능)
#튜플 자료형(순서, 중복 O 수정, 삭제 X)
#속도 튜플 > 리스트

#선언
a = []
b = list()
c = [0,0,1,2]
d = [0,1,'car','apple', 'apart']
e = [0,1,['car','apple','apart']]

a = ()
b = (0,)
c = (0,1,2,3)
d = (0,1,'car','apple', 'apart')
e = (0,1,('car','apple','apart'))

#인덱싱
print("####################")
print('d - ', type(d),d)
print('d - ', d[1])
print('d - ', d[0]+d[1]+d[1])
print('e - ', e[2][1])
print('e - ', e[-1][1])


#슬라이싱
print("####################")
print('d - ',d[0:3])
print('d - ',d[2:])


#연산
print("####################")
print('c + d', c+d)
print("c * 3", c * 3)
print('hi + c[0]', 'hi'+str(c[0]))

#리스트 수정 삭제
print("####################")
c[0] = 4
print('c - ',c)
c[1:2] = ['a','b','c']
print('c - ',c)
c[1] = ['a','b','c']
print('c - ',c)
c[1:3] = []
print('c - ',c)
del c[3]
print('c - ',c)


#리스트 함수
a = [5,2,3,1,4]
print("####################")
print("a - ", a)
a.append(6)
print("a - ", a)
a.sort()
print("a - ", a)
a.reverse()
print("a - ", a)
print("a - ", a.index(4), a[4])
print("a - ", a.count(3)) # a리스트에서 3의 갯수 확인
a.remove(2)
print("a - ", a)
print("a - ", a.pop()) #pop 하면 끝부터 나감
print("a - ", a)
ex = [8,9]
a.extend(ex)
print("a - ", a)

#리스트 삭제 방법: del, remove, pop

while a:
    l = a.pop()
    print(l is 4)
