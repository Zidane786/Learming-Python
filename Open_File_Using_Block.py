"""
   Block mai file open kerne ka yeh fayda hai ki hame close ke liye Open.close nhi likhna padega because ham jab
   block ka indent khatam kerege to matlab block waha band ho gaya jiska matlab wo file jo open ki thi wo bhi close ho gayi
"""
with open("Zidane.txt") as Open: #it is same as Open=open("Zidane.txt")
    Read=Open.read()
    print(Read)
"""
    Block khatam ho gaya matlab file bhi close ho jayegi
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