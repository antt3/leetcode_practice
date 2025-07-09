import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Initial Solution
    res_df = employee.sort_values(by="salary", ascending=False)[["salary"]].drop_duplicates()[1:2].set_axis(["SecondHighestSalary"], axis=1)
    return pd.DataFrame({"SecondHighestSalary": [None]}) if res_df.empty else res_df