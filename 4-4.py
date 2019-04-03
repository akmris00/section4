#딕셔너리 자료형(key, value) -> 순서 X 중복 X 수정 O 삭제 O

#선언
a = {'name':'kim', 'phone':'01077777777', 'birth':910809}
b = {0:'hello world'}
c = {'arr':[0,1,2,3]}

print(type(a), a)

#출력
print("a - ", a['name']) # 없으면 에러 발생
print("a - ", a.get('name')) # 없으면 None 리턴
print("c - ", c.get('arr'))

#딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1,2,3]
print('a - ', a)

print("a - ", a.keys())
print("a - ", list(a.keys()))

print("a - ", a.values())
print("a - ", list(a.values()))

print("a - ", a.items())
print("a - ", list(a.items())[0])

print("a - ", 'name' in a)
print("a - ", 'city' in a)
