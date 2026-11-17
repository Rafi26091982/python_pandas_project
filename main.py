import pandas as pd

from db_connection import get_connection

from analysis.employee_analysis import (
    total_employees,
    department_wise_count,
    location_wise_count,
    employee_status_count
)

from analysis.salary_analysis import (
    average_salary,
    maximum_salary,
    minimum_salary,
    department_average_salary,
    department_salary_summary
)


engine = get_connection()

query = "SELECT * FROM EMPLOYEES"

df = pd.read_sql(query, engine)

# Employee Analytics

print("Total Employees:", total_employees(df))

print("\nDepartment Wise Count:")
print(department_wise_count(df))

print("\nLocation Wise Count:")
print(location_wise_count(df))

print("\nEmployee Status:")
print(employee_status_count(df))


# Salary Analytics

print("\nAverage Salary:", average_salary(df))

print("\nMaximum Salary:", maximum_salary(df))

print("\nMinimum Salary:", minimum_salary(df))

print("\nDepartment Average Salary:")
print(department_average_salary(df))

print("\nDepartment Salary Summary:")
print(department_salary_summary(df))


engine.dispose()