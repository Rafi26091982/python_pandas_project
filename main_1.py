from analysis.employee_analysis import generate_employee_report
from analysis.salary_analysis import generate_salary_report


def main():

    print("Starting Oracle Pandas Analytics Project")

    print("\nGenerating Employee Report...")
    generate_employee_report()

    print("\nGenerating Salary Report...")
    generate_salary_report()

    print("\nAll reports generated successfully!")


if __name__ == "__main__":
    main()