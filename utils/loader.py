import pandas as pd
import pyreadr

def load_data(uploaded_file):

    name = uploaded_file.name.lower()

    if name.endswith(".csv"):

        return pd.read_csv(uploaded_file)

    elif name.endswith(".xlsx"):

        return pd.read_excel(uploaded_file)

    elif name.endswith(".xls"):

        return pd.read_excel(uploaded_file)

    elif name.endswith(".rds"):

        result = pyreadr.read_r(uploaded_file)

        return list(result.values())[0]

    elif name.endswith(".rdata"):

        result = pyreadr.read_r(uploaded_file)

        return list(result.values())[0]

    else:

        raise ValueError("Unsupported file.")
