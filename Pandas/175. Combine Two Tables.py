import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # Initial Solution
    return pd.merge(person, address, "left", "personId")[["firstName", "lastName", "city", "state"]]