import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students = students.astype({"grade": int})
    return students

# Improves memory at the expense of performance
# def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
#     students = students.astype({"grade": int}, False)
#     return students