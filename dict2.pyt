def dictionary_examples():
    print("\n--- DICTIONARY EXAMPLES ---")

    
    student = {
        "name": "Amit",
        "age": 22,
        "course": "BCA",
        "marks": 85
    }

    print("\nStudent Dictionary:", student)

    
    print("Name:", student["name"])
    print("Marks:", student.get("marks"))

    
    student["age"] = 23
    student["city"] = "Lucknow"
    print("Updated Student:", student)
