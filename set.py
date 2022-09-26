s = set(())
print(s)

s.add(1)
s.add(1)
print(s)
print(len(s))

s1 =({2,3})
print(s1)

s2 = s.union({1,2,3})
print(s2)

s3 = s.intersection({1,2,3,4,5,6})
print(s3)

print(s.isdisjoint(s1))
s1.add(1)
print(s.isdisjoint(s1))