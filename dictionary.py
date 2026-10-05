#DICTIONARY
student_data ={ 
    "name": "Alice",
    "age": 20,
    "DOD": "2003-1-15",
    "Location": "Nairobi",
    "Admission": "1234"
    }
print("Student Data:", student_data)

#FIND
print("Student Name:", student_data.get("name"))
print("Student Age:", student_data.get("age"))

#UPDATE
student_data.update({"age": 21})
print("Updated Student Age:", student_data.get("age"))
student_data.update({"Location": "Mombasa"})
print("Updated Student Location:", student_data.get("Location"))

#REMOVE
student_data.pop("DOD")
print("Student Data after removal:", student_data)

pop_item = student_data.popitem()
print("Removed Item:", pop_item)

clear_data = student_data.clear()
print("Student Data after clearing:", student_data)