#Dict comprehention
employees = [
    {"name": "John", "salary": 50000},
    {"name": "Jane", "salary": 60000},
    {"name": "Bob", "salary": 25000}]
salary_dict = {emp["name"]:emp["salary"] for emp in employees if emp["salary"]>30000
               }
print(salary_dict)