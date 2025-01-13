import pandas as pd

## First way: Using slicing
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[0:3]

## Second way: Using head
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
