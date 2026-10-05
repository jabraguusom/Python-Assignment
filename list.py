Student_names=[
    "Alice", 
    "Bob", 
    "Charlie", 
    "David", 
    "Eva", 
    "Frank", 
    "Grace", 
    "Hannah", 
    "Ian", 
    "Jack"
    ]
#Spliting the list into two parts
first_list=Student_names[0:5]
second_list=Student_names[5:10]

#Add
Student_names.append("Katherine")
#ADD for the two parts of the list
first_list.append("Tom")
second_list.append("Ummer")

#Remove
Student_names.remove("David")
Student_names.remove("Frank")

#Remove for the two parts of the list
first_list.remove("David")
second_list.remove("Hannah")

#numbers of Students in the list
student_num=len(Student_names)
print(Student_names)
print(student_num)
print(first_list)
print(second_list)

#List of Students in the list
List1=[1,2,3,4,5]
List2=[6,7,8,9,10]
Result=(List1+List2)
print(Result)
