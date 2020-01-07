"""
        Agar hame check kerna hai ke hamara jo file pointer hai jo ki niche wale case mai Open hai wo kaha pe hai
        to ham tell() method ka use kerege jo ke hame return dega Character  no. jaha pe hamara wo file pointer hai
"""
# Open=open("Zidane.txt")
# print(Open.tell())  # 0th Character pe hai hamara file pointer jo ki is case mai Open hai
# print(Open.readline(),end="")
# print(Open.tell())  # 16th Character pe hai hamara file pointer jo ki is case mai Open hai
# print(Open.readline(),end="")
# print(Open.tell())  # 39th Character pe hai hamara file pointer jo ki is case mai Open hai
# print(Open.readline(),end="")
# print(Open.tell())  # 69th Character pe hai hamara file pointer jo ki is case mai Open hai
# print(Open.readline(),end="")
# print(Open.tell())  # 106th Character pe hai hamara file pointer jo ki is case mai Open hai
# Open.close() #its good habbit to close when work is done
"""
            OUTPUT:-
                        0
                        Zidane is Great
                        16
                        Zidane is Really Great
                        39
                        Zidane is Really Really Great
                        69
                        Zidane is Really Really Really Great
                        106
"""


"""
        Agar hame jo file pointer hai usko position deni hai to hame seek() function use ker sekhte hai or ham seek function
        mai integer paas kerege jo ki character ka index hoga jaha pe hame hamara pointer set kerna hai
"""
# Open=open("Zidane.txt")
# print(Open.tell())  # at 0th Character
# print(Open.readline(),end="")
# print(Open.tell())  # at 16th Character
# Open.seek(0)        # Setting it at 0th Character by passing 0 in seek() function
# print(Open.tell())  # at 0th Character
# print(Open.readline(),end="")
# Open.close()
"""
            OUTPUT:-
                    0
                    Zidane is Great
                    16
                    0
                    Zidane is Great
"""

Open=open("Zidane.txt")
print(Open.read())  #isme file mai jo bhi hai wo print ho jayega
print(Open.readline())  # since jab ham read() use kiya to sab print ho gaya to ab kuch bacha nhi print kerne ka isliye yeh line ignore hogi because file pointer end mai hai

"""
            OUTPUT:-
                    Zidane is Great
                    Zidane is Really Great
                    Zidane is Really Really Great
                    Zidane is Really Really Really Great
                    Zidane is Really Really Really Really Great
                    Using Write Function in Append Mode
                    Using Write Function in Append Mode
                    Using Write Function in Append ModeI am Appending in Read and Write mode
"""