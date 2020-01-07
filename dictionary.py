#Dictionary:-It is Nothing but Key value pairs
# Dictionary Starts and close with Curly braces i.e:-{KEY:VALUE}
d1={}
print(type(d1)) #OUTPUT:-<class 'dict'>
d2={33:"Zidane",18:"Uzma",20:"Shamsher",30:"Vishal",28:"Sagar",15:"Deepyansh"}
print(d2)
print(d2.keys())#It Show number which represents values
print(d2.values()) #It show Values Stored
print(d2[33])#It print the value  of 33 key  OUTPUT:-Zidane
# We can even make a dictionary in a dictionary i.e:-
d3={33:"Zidane",18:"Uzma",20:"Shamsher",30:"Vishal",28:"Sagar",15:"Deepyansh","Others":{1:"Sneha Singh",2:"Sneha Gaikwad",3:"Aditi Patil",4:"Aditii Dalvi"}}
print(d3["Others"]) #OUTPUT:-{'Sneha:Singh', 'Aditi:Dalvi', 'Sneha:Gaikwad', 'Aditi:Patil'} as we see we print dictionary which was inside dictionary
#we can even print the value of the mini dictionary in following way i.e:-
print(d3["Others"][1]) #OUTPUT:-Sneha Singh /this is the way to acess mini dictionary
#For Addtion of ITEMS in Dictionary we will do this was as shown below i.e:-
d2[29]="Prathemesh"
print(d2) #OUTPUT:-{33: 'Zidane', 18: 'Uzma', 20: 'Shamsher', 30: 'Vishal', 28: 'Sagar', 15: 'Deepyansh', 29: 'Prathemesh'}
d2[31]="Jagruti"
d2[24]="Anish"
print(d2) #OUTPUT:-{33: 'Zidane', 18: 'Uzma', 20: 'Shamsher', 30: 'Vishal', 28: 'Sagar', 15: 'Deepyansh', 29: 'Prathemesh', 31: 'Jagruti', 24: 'Anish'}
d2[7.8]="Sadiya"
print(d2)
#IF WE WANT TO DELETE SPECIFIC KEY WE WILL DO AS SHOWN BELOW using del function i.e:-
del d2[7.8]
print(d2) #OUTPUT:-{33: 'Zidane', 18: 'Uzma', 20: 'Shamsher', 30: 'Vishal', 28: 'Sagar', 15: 'Deepyansh', 29: 'Prathemesh', 31: 'Jagruti', 24: 'Anish'} as we can see 7.8 key and his value Sadiya is deleted
#FUNCTIONS
#1:-COPY():
d4=d2
del d4[15]
print(d4) #OUTPUT:-{33: 'Zidane', 18: 'Uzma', 20: 'Shamsher', 30: 'Vishal', 28: 'Sagar', 29: 'Prathemesh', 31: 'Jagruti', 24: 'Anish'}
print(d2) #OUTPUT:-{33: 'Zidane', 18: 'Uzma', 20: 'Shamsher', 30: 'Vishal', 28: 'Sagar', 29: 'Prathemesh', 31: 'Jagruti', 24: 'Anish'}
"""
As we can see when we assingn d2 to d4 means d4 has same dictionary as d2 but when we delete a key from d4 and then 
print it than we can see that that key is deleted from d2 also its because the d2 and d4 are pointers which both points
on same dictionary that means when we delete element from d2 than it will be deleted from d4 and if we delete element 
from d4 than it will also be deleted from d2 for not facing that type of problem we use COPY funtion which copies 
dictionary d2 to d4 in which d2 and d4 pointer points on different dictionary at the place of pointing on same because 
we had made a copy of dictionary that means d2 and d4 are having different dictionary
"""
#we implement copy funtion using .copy() function
d4=d2.copy()
del d4[28]
print(d4) #OUTPUT:-{33: 'Zidane', 18: 'Uzma', 20: 'Shamsher', 30: 'Vishal', 29: 'Prathemesh', 31: 'Jagruti', 24: 'Anish'}
print(d2) #OUTPUT:-{33: 'Zidane', 18: 'Uzma', 20: 'Shamsher', 30: 'Vishal', 28: 'Sagar', 29: 'Prathemesh', 31: 'Jagruti', 24: 'Anish'}
#As we can see above deleting key from d4 does not effects d2
# 2:-GET(KEY):
#when we use get(key) function  and than it will print the VALUE of that print
print(d2.get(33)) #OUTPUT:-Zidane
# 3:-UPDATE(KEY:VALUE):
#when we use update() function we can update given dictionary by adding new key and its value
d1.update({28:"Sagar",31:"Jagruti"})
print(d1) #OUTPUT:-{28: 'Sagar', 31: 'Jagruti'}
# 4:-KEYS():
#it print all keys in dictionary
print(d1.keys()) #OUTPUT:-dict_keys([28, 31])
# 5:-VALUES():
#it print all values in dictionary
print(d1.values()) #OUTPUT:-dict_values(['Sagar', 'Jagruti'])
# 6:-ITEMS():
#key and its value will be print in tuple form
print(d1.items())