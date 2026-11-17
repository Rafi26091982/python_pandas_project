import pandas as pd


def average_salary(df):

    return df["salary"].mean()


def maximum_salary(df):

    return df["salary"].max()


def minimum_salary(df):

    return df["salary"].min()


def department_average_salary(df):

    result = df.groupby("department")["salary"].mean()

    return result


def department_salary_summary(df):

    result = df.groupby("department")["salary"].agg(
        ["count", "mean", "min", "max", "sum"]
    )