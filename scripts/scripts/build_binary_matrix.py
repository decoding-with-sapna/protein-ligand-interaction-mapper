import pandas as pd

def build_binary_matrix(df):
    df["Residue"] = df["Residue_Name"] + "_" + df["Residue_Number"]

    binary = pd.crosstab(df["Residue"], df["Interaction_Type"])
    binary[binary > 0] = 1

    return binary
