"""
Create a Dictionary take input from the USER and RETURN the Meaning  of the word from the
Dictionary
"""
D={33: 'Zidane', 18: 'Uzma', 20: 'Shamsher', 30: 'Vishal', 28: 'Sagar', 15: 'Deepyansh', 29: 'Prathemesh', 31: 'Jagruti', 24: 'Anish', 7.8: 'Sadiya'}
print("Enter the key:-")
c=int(input())
print("The Key enter is",end=" ")
print(c,"its value ",end="is ")
print(D[c])
"""
                        OR
print(D[int(input("Enter Key:-"))])
"""