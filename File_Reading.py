            #  ***Open File and Reading it as text file***:-
# open_file=open("Zidane.txt", 'rt')  # In this rt is Default where r is read and t is text
# Read_File=open_file.read()
# print(Read_File)
# open_file.close() # It is good habbit to close the file when work is done Because we need to free Memomy when our work is done
"""
        OUTPUT:-
                Zidane is Great
                Zidane is Really Great
                Zidane is Really Really Great
                Zidane is Really Really Really Great
                Zidane is Really Really Really Really Great
"""
            #  ***Read And Binary*** :-
# open_file1=open("Zidane.txt","rb")
# Read_File1=open_file1.read()
# print(Read_File1)  # Give Output in Binary String Form

"""
        OUTPUT:-
                b'Zidane is Great\nZidane is Really Great\nZidane is Really Really Great\nZidane is Really Really Really Great\nZidane is Really Really Really Really Great'
                
"""

            #  ***passing Argument in read functoion***:-
# Open=open("Zidane.txt")
# Read=Open.read(2)
# print(Read)
# Read=Open.read(3)
# print(Read)  # pehle jab read mai 2 paas kiya to Zi ho gaya tha ab 3 paas kiya to uske aage se lege i.e dan See Output for better understanding


"""
        OUTPUT:-
                Zi
                dan
"""

            #  ***If we want to print Content of file line by line we can do by following way***:-
# Open=open("Zidane.txt")
# for line in Open:
#     print(line,end="")

"""
        OUTPUT:-
                Zidane is Great
                Zidane is Really Great
                Zidane is Really Really Great
                Zidane is Really Really Really Great
                Zidane is Really Really Really Really Great
"""

            # *** readline() Function***:-
# Open=open("Zidane.txt")
# print(Open.readline(),end="")   #It read a line agar hame multiple line read kerni hai to isse multiple time read kerna padega readline()=read a single line
# print(Open.readline(),end="")   # uske saath new line character bhi read kerta hai isliye hame end="" lagayege
# print(Open.readline(),end="")
# print(Open.readline(),end="")
# print(Open.readline(),end="")
"""
        OUTPUT:-
                Zidane is Great
                Zidane is Really Great
                Zidane is Really Really Great
                Zidane is Really Really Really Great
                Zidane is Really Really Really Really Great
"""

            # *** readlines() Function(it create list)***:-
Open=open("Zidane.txt")
print(Open.readlines())  #hamari har line List mai store ho jayegi with new line character
"""
        OUTPUT:-
                ['Zidane is Great\n', 'Zidane is Really Great\n', 'Zidane is Really Really Great\n', 'Zidane is Really Really Really Great\n', 'Zidane is Really Really Really Really Great']
"""

Open.close()  #good habbit to close it when work is done