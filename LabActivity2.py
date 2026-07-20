def check_fast_lane(minutes_left, items, teacher_pass):
    if teacher_pass == True:
        return "Fast lane approved"
    elif minutes_left < 10 and items <= 3:
        return "Fast lane approved"
    else:
        return "Use regular line"

fast_lane_counter = 0

students_in_line = [
    {"name": "Marco", "minutes_left": 8, "items": 2, "teacher_pass": False},
    {"name": "Diane", "minutes_left": 15, "items": 1, "teacher_pass": False},
    {"name": "Kyle", "minutes_left": 5, "items": 6, "teacher_pass": False},
    {"name": "Ella", "minutes_left": 20, "items": 5, "teacher_pass": True},
]

for student in students_in_line:
    name = student["name"]
    minutes_left = student["minutes_left"]
    items = student["items"]
    teacher_pass = student["teacher_pass"]
    
    result = check_fast_lane(minutes_left, items, teacher_pass)
    
    if result == "Fast lane approved":
        fast_lane_counter = fast_lane_counter + 1
        print(name + ": Fast lane approved")
    else:
        print(name + ": Use regular line - you have " + str(minutes_left) + " minutes left")

print()
print("Total students who used fast lane:", fast_lane_counter)

