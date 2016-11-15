# dict
s = {'lsqy': 98,'yun': 99}
print(s['lsqy']) # 98

print('aa' in s) # False

print(s.get('aa',10)) # 10
# print(s['aa']) # error

# set
d = set([1,2,3])
print(d) # {1, 2, 3}
e = set([2,2,3,3,4,4,5,5])
print(e) # {2, 3, 4, 5}

e.add(10)
print(e) # {10, 2, 3, 4, 5}

e.remove(4)
print(e) # {10, 2, 3, 5}

a = set([4,5,6])
b = set([5,6,7])
print(a & b) # {5,6}
print(a | b) # {4,5,6,7}