# Open=open("Zidane2.txt","w")  #We open file in Writing mode
# Open.write("Using Write Fucntion in Write Mode")
# Open.close()
"""
        yeh write mode mai write fiunction se  pehle agar kuch likha hua hai file mai to wo nikal jayega or jo write Function mai likha hai wo aa jayega
        Agar jo naam ki file open ki hai agar wo exist hi nhi kerti since ham write mode mai file open ker rahe hai isliye jo naam likha hai open mai 
        wo naam ki file ban jayegi or fir wo write function mai jo likha hai wo uss file mai aa jayega
"""
#Generally hame kuch append kerna hota hai existing file mai to wo kuch is tarah kerege jaisa niche kiya hai:-
"""
        Agar hame koi existing file mai kuch append kerna hai to ham file ko append mode mai open kerege i.e:-"a" mode mai
        we are opening Zidane.txt before appending uska data kuch aisa hai
        Data in Zidane.txt:-
                            Zidane is Great
                            Zidane is Really Great
                            Zidane is Really Really Great
                            Zidane is Really Really Really Great
                            Zidane is Really Really Really Really Great
"""
# Open=open("Zidane.txt","ar")
# Open.write("\nUsing Write Function in Append Mode") #Jitni baar bhi ham run kerege ootni baar yeh add hota rahega file mai
# Open.close()
"""
        Maine isko 3 baar run kiya isliye yeh line 3 baar aa gayi mere file mai
        Data in Zidane.txt After Appending using Append Mode:-
                                                                Zidane is Great
                                                                Zidane is Really Great
                                                                Zidane is Really Really Great
                                                                Zidane is Really Really Really Great
                                                                Zidane is Really Really Really Really Great
                                                                Using Write Function in Append Mode
                                                                Using Write Function in Append Mode
                                                                Using Write Function in Append Mode
"""

            # Read and Write both
Open=open("Zidane.txt","r+") #r+ is read and write both mode
"""
        Read and Write both mode mai ham file ko read bhi ker sekhte hai or usme kuch append bhi ker sekhte hai
        Data in Zidane.txt :-
                                Zidane is Great
                                Zidane is Really Great
                                Zidane is Really Really Great
                                Zidane is Really Really Really Great
                                Zidane is Really Really Really Really Great
                                Using Write Function in Append Mode
                                Using Write Function in Append Mode
                                Using Write Function in Append Mode
"""
Read=Open.read()  # We are reading content in file
print(Read)
Open.write("I am Appending in Read and Write mode")
Open.close()
"""
            Now the Updated Data of file is:-
                                                Zidane is Great
                                                Zidane is Really Great
                                                Zidane is Really Really Great
                                                Zidane is Really Really Really Great
                                                Zidane is Really Really Really Really Great
                                                Using Write Function in Append Mode
                                                Using Write Function in Append Mode
                                                Using Write Function in Append ModeI am Appending in Read and Write mode
"""