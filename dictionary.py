#dictionary

d1 = {'sub1':'kannada','sub2':'english','sub3':'hindi'}
print(d1)
print(d1['sub1'])
d2 ={'sub1':'kannada','sub2':'english','sub3':'hindi','sub4':{'social':'history','science':'physics'}}
print(d2)
print(d2['sub4'])
print(d2['sub4']['social'])
d2['sub6']='maths'
print(d2)

del d1['sub2']
print(d1)

d1.update({'sub2':'english'})
print(d1)
d1.update({'sub2':'eng'})
print(d1)
print(' ')
print(d1.keys())
print(d1.values())

a = {'sub1':'kannada','sub2':'english','sub3':'hindi','sub4':'social','sub5':'science','sub6':'maths','sub7':'drawing','sub8':'8'}
print('enter key: ')
keys = input()
print(a[keys])