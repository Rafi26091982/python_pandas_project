
import pandas as pd

from db_connection import get_connection


def generate_salary_report():

    engine = get_connection()

    query = """
        SELECT
            EMPLOYEE_ID,
            FIRST_NAME,
            LAST_NAME,
            DEPARTMENT,
            JOB_TITLE,
            SALARY,
            LOCATION
        FROM EMPLOYEES
    """

    df = pd.read_sql(query, engine)

    # Department-wise salary analysis
    salary_summary = (
        df.groupby("department")["salary"]
        .agg(
            total_salary="sum",
            average_salary="mean",
            minimum_salary="min",
            maximum_salary="max",
            employee_count="count"
        )
        .reset_index()
    )

    # Highest salary employees
    highest_salary = df.nlargest(5, "salary")

    # Overall salary statistics
    overall_summary = df["salary"].describe().to_frame(
        name="Salary Statistics"
    )

    # Export Excel
    with pd.ExcelWriter(
        "reports/salary_report.xlsx",
        engine="openpyxl"
    ) as writer:

        df.to_excel(writer, sheet_name="Salary Details", index=False)

        salary_summary.to_excel(
            writer,
            sheet_name="Department Salary",
            index=False
        )

        highest_salary.to_excel(
            writer,
            sheet_name="Top 5 Salaries",
            index=False
        )

        overall_summary.to_excel(
            writer,
            sheet_name="Overall Summary"
        )

    engine.dispose()

    print("Salary report generated successfully!")