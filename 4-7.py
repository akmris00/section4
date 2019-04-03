import simplejson as json
#import json

#dict(json)선언

data = {}
data['people'] = []
data['people'].append({
    'name':'kim',
    'website':'naver.com',
    'From':'Seoul',
    'grade':[95,77,89,91]
})
data['people'].append({
    'name':'park',
    'website':'google.com',
    'From':'Busan',
    'grade':[85,67,100,93]
})
data['people'].append({
    'name':'lee',
    'website':'daum.com',
    'From':'Incheon',
    'grade':[98,79,58,75]
})

#json 파일 쓰기(dump)
with open('c:/Atom/section4/member_1.json', 'w') as outfile:
    json.dump(data, outfile)

with open('c:/Atom/section4/member_1.json', 'r') as infile:
    r = json.load(infile)
    #print(r)
    print('============')
    for p in r['people']:
        print('name: ' + p['name'])
        print('website: ' + p['website'])
        print('From: ' + p['From'])
        t = p['grade']
        grade = ''
        for g in t:
            grade = grade + ' ' + str(g)
        print('grade: ',grade.lstrip())
