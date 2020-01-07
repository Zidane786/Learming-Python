s=set()
s1=set()
print(type(s)) #OUTPUT:-<class 'set'>
k=[1,3,5,7,9,11]
s_from_list=set(k)
print(s_from_list) #OUTPUT:-{1, 3, 5, 7, 9, 11}
print(type(s_from_list)) #OUTPUT:-<class 'set'>
#set take only unique values it means it doesnot have same value i.e:- if we add 1 two time using add() we will get only one 1 but if we add 1 & 2 using add() than both 1,2 will be printed
#e.g:-
s.add(1)
s.add(1)
print(s) #OUTPUT:-{1}
s1.add(1) #ADD FUNCTION
s1.add(2)
s1.add(3)
print(s1) #OUTPUT:-{1, 2, 3}
s2=s1.union({1,2,3,4}) #UNION FUNCTION
print(s1,s2)#OUTPUT:-{1, 2, 3} {1, 2, 3, 4}
s2=s1.intersection({1,2,3,4})
print(s1,s2) #OUTPUT:-{1, 2, 3} {1, 2, 3}
s2={5,23,21}
print(s1.isdisjoint(s2)) #isdisjoint() function means values in that should be different
s1.remove(2)
print(s1)
