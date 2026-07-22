import json

# Open and read the JSON file
with open("student.json", "r") as file:
    student = json.load(file)

# Get student name and subjects
name = student["name"]
subjects = student["subjects"]

# Assume student has passed initially
overall_result = "PASS"

print("------ Subject Result ------")

# Loop through subjects
for subject, marks in subjects.items():

    if marks >= 40:
        result = "PASS"
    else:
        result = "FAIL"
        overall_result = "FAIL"

    print(f"{subject} : {marks} -> {result}")

# Create report dictionary
report = {
    "name": name,
    "overall_result": overall_result
}

# Write report to a new JSON file
with open("student_report.json", "w") as file:
    json.dump(report, file, indent=4)

print("\nStudent report created successfully.")