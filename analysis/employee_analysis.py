import pandas as pd

from db_connection import get_connection


def generate_employee_report():

    engine = get_connection()

    query = """
        SELECT
            EMPLOYEE_ID,
            FIRST_NAME,
            LAST_NAME,
            EMAIL,
            DEPARTMENT,
            JOB_TITLE,
            LOCATION,
            STATUS,
            HIRE_DATE
        FROM EMPLOYEES
    """

    df = pd.read_sql(query, engine)

    # Department-wise employee count
    dept_count = (
        df.groupby("department")
        .size()
        .reset_index(name="employee_count")
    )

    # Location-wise employee count
    location_count = (
        df.groupby("location")
        .size()
        .reset_index(name="employee_count")
    )

    # Status-wise employee count
    status_count = (
        df.groupby("status")
        .size()
        .reset_index(name="employee_count")
    )

    # Export to Excel
    with pd.ExcelWriter(
        "reports/employee_report.xlsx",
        engine="openpyxl"
    ) as writer:

        df.to_excel(writer, sheet_name="Employee Details", index=False)

        dept_count.to_excel(writer, sheet_name="Department Summary", index=False)

        location_count.to_excel(writer, sheet_name="Location Summary", index=False)

        status_count.to_excel(writer, sheet_name="Status Summary", index=False)

    engine.dispose()

    print("Employee report generated successfully!")