import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Simplified Solution
    sorted_salaries = employee['salary'].sort_values(ascending=False).drop_duplicates()
    return pd.DataFrame({
        'SecondHighestSalary': [None if sorted_salaries.size < 2 else sorted_salaries.iloc[1]]
    })
    
    # Initial Solution
    # res_df = employee.sort_values(by="salary", ascending=False)[["salary"]].drop_duplicates()[1:2].set_axis(["SecondHighestSalary"], axis=1)
    # return pd.DataFrame({"SecondHighestSalary": [None]}) if res_df.empty else res_df