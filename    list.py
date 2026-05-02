list=[1,"2",2.5,4,5]
print(type(list))
print(list[0])
list.append(4)
print(list)
list.insert(2,6)
print(list)
list.extend([7,8,9])
print(list)
print(list.count(4))
print(list.index(5))
list.remove(9)
print(list)
list.pop()
print(list)
list.pop(3)
print(list)
list.remove(4)
print(list)
list.clear()
print(list)

#list=[45,78,25,36,96,45,82,53]
#list.sort()
#print(list)
#list.reverse()
#print(list)
#print(len(list))
#print(max(list))
#print(min(list))
#print(sum(list))


#list=[1,2,3,4,5]
#nlist=list.copy()
#nlist[0]=6
#print(list)
#print(nlist)

#tuple
#tpl=(1,2,3,4,5)
#print(type(tpl))
#t=1,2,3
#print(type(t))
#t=(6,)
#print(type(t))
#print(tpl.count(5))
#print(tpl.index(5))
#stpl=sorted(tpl,reverse=True)
#print(stpl)
#stpl=sorted(tpl)
#print(tpl)


#set
#s={25,42,85,35,12,45,96,85,32,45,78,65,96,32,54,45}
#print(s)
#s=set()
#print(type(s))
#s.add(5)
#print(s)
#s.update([6,7,8,8,9,10,11,12])
#print(s)
#s.remove(5)
#print(s)
#s.discard(13)
#print(s)
#s.pop()
#print(s)
#s.clear()
#print(s)


#a={1,2}
#b={3,4,5}
#a=a.union(b)
#print(a)
#b.add(6)
#print(b)
#print(a.intersection(b))
#print(a.difference(b))
#print(a.symmetric_difference(b))

#a={1,2}
#b={1,2,3,4,5}
#print(a.issubset(b))
#print(b.issuperset(a))
#print(a.isdisjoint(b))

#dictionery
#d={"a":1}
#d["b"]=2
#print(d)
#d["a"]=3
#print(d)
#d[4]=5
#print(d)
#d[(1,2)]="str"
#print(d)
#d[(1,[2])]="str"
#print(d)

d={1:"sunday",2:"monday",3:"tuesday",4:"wednesday"}

#print(d[1])
#d.pop(2)
#print(d)
#d.popitem()
#print(d)
#print(d.keys())
#print(d.values())
#d.clear()
#print(d)


