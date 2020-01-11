name = list()  # name=[]
num = int(input("Enter number of Students:-"))
for i in range(1, num + 1):
    print(f"Enter the name of Student {i}:-")
    nameList = input()
    name.append(nameList)
# print(name)
marks = list()  # it will contain as much list as per  the students
temp_marks = list()  # it will contain marks of individual student as a single list which is empty right now
for i in range(0,
               num):  # Marks of each student will assign to a seperate list we will clear temp_marks every time in for loop using temp_marks.clear()
    print(f"Enter marks of Python out of 100 for {name[i]}:-")
    python = int(input())
    temp_marks.append(python)
    print(f"Enter marks of java for out of 100 {name[i]}:-")
    java = int(input())
    temp_marks.append(java)
    print(f"Enter marks of SQL for out of 100 {name[i]}:-")
    SQL = int(input())
    temp_marks.append(SQL)
    print(f"Enter marks of CSS for out of 100 {name[i]}:-")
    CSS = int(input())
    temp_marks.append(CSS)
    print(f"Enter marks of Javacsript for out of 100 {name[i]}:-")
    javascript = int(input())
    temp_marks.append(javascript)
    name_copy = temp_marks.copy()  # we had list temp_marks which will get copy to name_copy
    marks.append(name_copy)  # we will append the name_copy() to marks
    temp_marks.clear()  # we will clear temp_marks so it can take other student marks as a list
# print(marks)
# print(marks[0])
data_of_marks_per_subject = dict()  # we will create dictionary where each student will represent its marks list
for i in range(0, len(name)):
    data_of_marks_per_subject.update({name[i]: marks[i]})
# print(data_of_marks_per_subject)
total = list()  # it will take total of every student in list
for k, v in data_of_marks_per_subject.items():
    # print(f"{k} total marks is {sum(v)} out of ",500)
    temp_total = sum(v)  # we assing sum to a temporary variable temp_total
    total.append(temp_total)  # we will append temp_total to total
# print(total)
data_for_total_marks = dict()  # we will create dictionary where each student will represent its sum of marks list
for i in range(0, len(name)):
    data_for_total_marks.update({name[i]: total[i]})
# print(data_for_total_marks)

result = dict()
KT = dict()
for k, v in data_of_marks_per_subject.items():
    # print(k, ":", v)
    count = 0
    for i in range(0, 5):
        # print(v[i])
        if (v[i] < 40):
            count = count + 1

    if (count > 0):
        if (count == 1):
            for i in range(0, 5):
                if ( v[i] >= 30 ):
                    if ( v[i] >= 30 and v[i] <= 40):
                        grace_marks=40-v[i]
                        count = count - 1
                        v[i] += grace_marks
                        print(f"{k} got {grace_marks} grace marks")
                        res1 = "Pass"
                        result.update({k: res1})
                        KT.update({k: count})
                if (v[i] <= 29):
                    res = "Fail"
                    result.update({k: res})
                    KT.update({k: count})
        else:
            res = "Fail"
            result.update({k: res})
            KT.update({k: count})
    else:
        res = "Pass"
        result.update({k: res})
        KT.update({k: count})
# print(result)
average = list()  # it will take average of every student in list
for k, v in data_for_total_marks.items():
    # print(f"{k} average mark is {v/5}")
    temp_average = v / 5  # average of student is store in temp_average
    average.append(temp_average)  # we will append temp_average to average list
# print(temp_average)
data_for_average = dict()
for i in range(0, len(name)):
    data_for_average.update({name[i]: average[i]})
# print(data_for_average)
# print(temp_average)
percentage = list()
for k, v in data_for_total_marks.items():
    # print(f"{k} got {(v/500)*100} percentage")
    temp_percentage = (v / 500) * 100
    temp_percentage=format(temp_percentage , ".2f")
    percentage.append(temp_percentage)
# print(percentage)
data_for_percentage = dict()
for i in range(0, len(name)):
    data_for_percentage.update({name[i]: percentage[i]})
# print(data_for_percentage)
sorted_percentage = dict()
for k, v in sorted(data_for_percentage.items(), key=lambda item: item[1]):
    sorted_percentage.update({k: v})
# print(sorted_percentage)
rank = list()
for i in range(1, num + 1):
    z = input("ranks as from A to N Students")
    rank.append(z)
rank.reverse()
# print(rank)
name_for_rank = list()
for k in sorted_percentage.keys():
    name_for_rank.append(k)
ranked_Student = dict()
for i in range(0, len(name)):
    ranked_Student.update({name_for_rank[i]: rank[i]})
# print(ranked_Student)
sorted_ranked_student = dict()
for k, v in ranked_Student.items():
    dict_element = {k: v}
    dict_element.update(sorted_ranked_student)
    sorted_ranked_student = dict_element


# print(sorted_ranked_student)
def Result():
    print("********** Marks Are:-*********")
    for k, v in data_of_marks_per_subject.items():
        print(f"--- {k} marks:- ---")
        print(f"Python={v[0]}")
        print(f"Java={v[1]}")
        print(f"SQL={v[2]}")
        print(f"CSS={v[3]}")
        print(f"JavaScript={v[4]}")
        print("--------------------")
    print("*****************************")
    print("********** Total Marks Are:-*********")
    for p, q in data_for_total_marks.items():
        print(f"{p} Total marks are {q}")
    print("*****************************")
    print("********** Average Marks Are:-*********")
    for z, u in data_for_average.items():
        print(f"{z} average marks are {u}")
    print("*****************************")
    print("********** Percentage Are:-*********")
    for s, d in data_for_percentage.items():
        print(f"{s} got {d} percentage")
    print("*****************************")
    print("********** Result:-*********")
    for i, j in result.items():
        print(f"{i} is {j}")
    print("*****************************")
    print("********** Number of KTs :-*********")
    for a, b in KT.items():
        print(f"{a} got {b} KT")
    print("*****************************")
    print("***************************** Ranks are *****************************")
    for w, o in sorted_ranked_student.items():
        print(f"{w} got Ranked:-{o}")
    print("*********************************************************************")


Result()


#----->OUTPUT:-
# "/home/zidane/PycharmProjects/Learning 1/venv/bin/python" "/home/zidane/PycharmProjects/Learning 1/Student.py"
# Enter number of Students:-5
# Enter the name of Student 1:-
# Zidane
# Enter the name of Student 2:-
# Uzma
# Enter the name of Student 3:-
# Shamsheer
# Enter the name of Student 4:-
# Vishal
# Enter the name of Student 5:-
# Deepyansh
# Enter marks of Python out of 100 for Zidane:-
# 100
# Enter marks of java for out of 100 Zidane:-
# 100
# Enter marks of SQL for out of 100 Zidane:-
# 98
# Enter marks of CSS for out of 100 Zidane:-
# 30
# Enter marks of Javacsript for out of 100 Zidane:-
# 95
# Enter marks of Python out of 100 for Uzma:-
# 100
# Enter marks of java for out of 100 Uzma:-
# 100
# Enter marks of SQL for out of 100 Uzma:-
# 100
# Enter marks of CSS for out of 100 Uzma:-
# 100
# Enter marks of Javacsript for out of 100 Uzma:-
# 100
# Enter marks of Python out of 100 for Shamsheer:-
# 90
# Enter marks of java for out of 100 Shamsheer:-
# 80
# Enter marks of SQL for out of 100 Shamsheer:-
# 79
# Enter marks of CSS for out of 100 Shamsheer:-
# 30
# Enter marks of Javacsript for out of 100 Shamsheer:-
# 30
# Enter marks of Python out of 100 for Vishal:-
# 90
# Enter marks of java for out of 100 Vishal:-
# 85
# Enter marks of SQL for out of 100 Vishal:-
# 34
# Enter marks of CSS for out of 100 Vishal:-
# 94
# Enter marks of Javacsript for out of 100 Vishal:-
# 94
# Enter marks of Python out of 100 for Deepyansh:-
# 90
# Enter marks of java for out of 100 Deepyansh:-
# 85
# Enter marks of SQL for out of 100 Deepyansh:-
# 29
# Enter marks of CSS for out of 100 Deepyansh:-
# 84
# Enter marks of Javacsript for out of 100 Deepyansh:-
# 84
# Zidane got 10 grace marks
# Vishal got 6 grace marks
# ranks as from A to N StudentsA
# ranks as from A to N StudentsB
# ranks as from A to N StudentsC
# ranks as from A to N StudentsD
# ranks as from A to N StudentsE
# ********** Marks Are:-*********
# --- Zidane marks:- ---
# Python=100
# Java=100
# SQL=98
# CSS=40
# JavaScript=95
# --------------------
# --- Uzma marks:- ---
# Python=100
# Java=100
# SQL=100
# CSS=100
# JavaScript=100
# --------------------
# --- Shamsheer marks:- ---
# Python=90
# Java=80
# SQL=79
# CSS=30
# JavaScript=30
# --------------------
# --- Vishal marks:- ---
# Python=90
# Java=85
# SQL=40
# CSS=94
# JavaScript=94
# --------------------
# --- Deepyansh marks:- ---
# Python=90
# Java=85
# SQL=29
# CSS=84
# JavaScript=84
# --------------------
# *****************************
# ********** Total Marks Are:-*********
# Zidane Total marks are 423
# Uzma Total marks are 500
# Shamsheer Total marks are 309
# Vishal Total marks are 397
# Deepyansh Total marks are 372
# *****************************
# ********** Average Marks Are:-*********
# Zidane average marks are 84.6
# Uzma average marks are 100.0
# Shamsheer average marks are 61.8
# Vishal average marks are 79.4
# Deepyansh average marks are 74.4
# *****************************
# ********** Percentage Are:-*********
# Zidane got 84.60 percentage
# Uzma got 100.00 percentage
# Shamsheer got 61.80 percentage
# Vishal got 79.40 percentage
# Deepyansh got 74.40 percentage
# *****************************
# ********** Result:-*********
# Zidane is Pass
# Uzma is Pass
# Shamsheer is Fail
# Vishal is Pass
# Deepyansh is Fail
# *****************************
# ********** Number of KTs :-*********
# Zidane got 0 KT
# Uzma got 0 KT
# Shamsheer got 2 KT
# Vishal got 0 KT
# Deepyansh got 1 KT
# *****************************
# ***************************** Ranks are *****************************
# Zidane got Ranked:-A
# Vishal got Ranked:-B
# Deepyansh got Ranked:-C
# Shamsheer got Ranked:-D
# Uzma got Ranked:-E
# *********************************************************************

# Process finished with exit code 0
