import simplejson as json
#import json

#dict(json)선언

data = {}
data['people'] = []
data['people'].append({
    'name':'kim',
    'website':'naver.com',
    'From':'Seoul'
})
data['people'].append({
    'name':'park',
    'website':'google.com',
    'From':'Busan'
})
data['people'].append({
    'name':'lee',
    'website':'daum.com',
    'From':'Incheon'
})

#print(data)

#dict(json) -> str
e = json.dumps(data)
e = json.dumps(data, indent=4)
#print(type(e))
#print(e)

#str -> dict(json)
d = json.loads(e)
#print(type(d))
#print(d)

with open('c:/Atom/section4/member.json', 'w') as outfile:
    outfile.write(e)

with open('c:/Atom/section4/member.json', 'r') as infile:
    r = json.loads(infile.read())
    #print("==========")
    #print(r)
    for p in r['people']:
        print('name: ' + p['name'])
        print('website: ' + p['website'])
        print('From: ' + p['From'])
