import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    new_df = employees.copy()
    new_df["salary"] = new_df["salary"] * 2
    return new_df
