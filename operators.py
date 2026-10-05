import numpy as np
import array as array

list1 = [20, 25, 30, 35, 40]
list2 = [45, 50, 55, 60, 65]

#ADDITION
#Addition of two lists
result = list1 + list2
print("Result of adding two lists:", result)
#Convert the lists to NumPy arrays
list1_np = np.array(list1)
list2_np = np.array(list2)
#Addition of two elements in NumPy arrays
result_np = list1_np + list2_np
print("Result of adding two NumPy arrays:", result_np)


num_students = len(list1) + len(list2)
print("Total number of students:", num_students)

#UPDATE
# Add new elements to the NumPy array
updated_list1_np = np.append(list1_np, (21, 22, 23, 24))
updated_list2_np = np.append(list2_np, (66, 67, 68, 69))
result_np1 = updated_list1_np + updated_list2_np

print("Updated NumPy array:", updated_list1_np)
print("Updated NumPy array:", updated_list2_np)
print("Total number of students after adding new elements:", len(updated_list1_np) + len(updated_list2_np))
print("Result of adding two NumPy arrays after updating:", result_np1)

#SUBTRACTION
result_sub = list2_np - list1_np
print("Result of subtracting two NumPy arrays:", result_sub)

updated_result_sub = updated_list2_np - updated_list1_np
print("Result of subtracting two updated NumPy arrays:", updated_result_sub)

#MULTIPLICATION
result_mul = list1_np * list2_np
print("Result of multiplying two NumPy arrays:", result_mul)

updated_result_mul = updated_list1_np * updated_list2_np
print("Result of multiplying two updated NumPy arrays:", updated_result_mul)


#DIVISION
div_result = list2_np / list1_np

updated_div_result = updated_list2_np / updated_list1_np

for up_result in updated_div_result:
    print(up_result)