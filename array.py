import array as array
import numpy as np

#List of student ages in Arra
student_ages=array.array('i', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29])

#Substitute the list age of the students into a NumPy array
student_ages_np=np.array(student_ages)

#Calculate the age of the students after two years as array and NumPy array
two_years=array.array('i', [age + 2 for age in student_ages])
in_two_years_np=student_ages_np + 2
in_two_Decade_np=student_ages_np + 10*2
#count the number of students in the list
num_students=len(student_ages)
#Display the results\\
print("Students' Ages:", student_ages)
print("After two years Students Age:", two_years)
print("After two years Students Age as NumPy:", in_two_years_np)
print("After two decades Students Age as NumPy:", in_two_Decade_np)
print("Number of Students:", num_students)
