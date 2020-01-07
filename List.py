#LIST:-It is Mutable i.e:-It can be Change i.e:-We can Change values in List
#List Starts and Close with Sqaure Brackets
zid=["Zidane","Uzma","Vishal","Shamsher","Sagar","Deepyansh"]
print(zid[0:4])
zid1=["Zidane",33,"Uzma",18,"Shamsher",20,"Vishal",30,"Deepyansh", 15]
zid2=[7,8,9,10,20,30,25]
zid.sort()
zid.reverse()
zid1.reverse()
print(zid)
print(zid1)
print(len(zid))
print(len(zid1))
# Slicing
print(zid[0:2])
print(zid)
# Extended Slice
zid1.reverse()
print(zid1[::2])
# To add anything in List we use Append
zid2.append(29)
print(zid2)
zid2.pop() # Delete last element of this List
print(zid2)