name=list()
num=int(input("Enter number of Students:-"))
for i in range(1,num+1):
    print(f"Enter the name of Student {i}:-")
    nameList=input()
    name.append(nameList)
print(name)
marks=list()
temp_marks=list()
for i in range(0,num):
    print(f"Enter marks of Python out of 100 for {name[i]}:-")
    python=int(input())
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
    name_copy=temp_marks.copy()
    marks.append(name_copy)
    temp_marks.clear()
print(marks)
# print(marks[0])
data_of_marks_per_subject=dict()
for i in range(0,len(name)):
    data_of_marks_per_subject.update({name[i]:marks[i]})
print(data_of_marks_per_subject)
total=list()
for k,v in data_of_marks_per_subject.items():
    print(f"{k} total marks is {sum(v)} out of ",500)
    temp_total=sum(v)
    total.append(temp_total)
print(total)
data_for_total_marks=dict()
for i in range(0,len(name)):
    data_for_total_marks.update({name[i]:total[i]})
print(data_for_total_marks)
average=list()
for k,v in data_for_total_marks.items():
    print(f"{k} average mark is {v/5}")
    temp_average=v/5
    average.append(temp_average)
print(temp_average)
data_for_average=dict()
for i in range(0,len(name)):
    data_for_average.update({name[i]:average[i]})
print(data_for_average)
print(temp_average)
percentage=list()
for k,v in data_for_total_marks.items():
    print(f"{k} got {(v/500)*100} percentage")
    temp_percentage=(v/500)*100
    percentage.append(temp_percentage)
print(percentage)
data_for_percentage=dict()
for i in range(0,len(name)):
    data_for_percentage.update({name[i]:percentage[i]})
print(data_for_percentage)
sorted_percentage=dict()
for k,v in sorted(data_for_percentage.items()):
    sorted_percentage.update({k:v})


print(sorted_percentage)
rank=list()
for i in range(1,num+1):
    z=input("ranks as from A to n Students")
    rank.append(z)
print(rank)
