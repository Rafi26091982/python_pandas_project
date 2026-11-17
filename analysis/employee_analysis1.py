import pandas as pd


def total_employees(df):

    return len(df)


def department_wise_count(df):

    result = df.groupby("department").size()

    return result


def location_wise_count(df):

    result = df.groupby("location").size()

    return result


def employee_status_count(df):

    result = df.groupby("status").size()

    return result