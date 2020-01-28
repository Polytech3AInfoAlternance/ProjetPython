import pandas as pd


def csv_to_df(path, rows):
    df = pd.read_csv(path, encoding="ISO-8859-1", skiprows=[i for i in range(1, 10)])
    df_split = df["[HEADER]"].str.split(";", expand=True)
    columns = df_split.iloc[0]
    fields = ["Date"]
    indexToStore = [0]
    for j in range(1, len(columns)):
        for value in rows:
            if columns[j] == value:
                #print(value)
                indexToStore.append(j)
    df_result = df_split[indexToStore]
    for i in range(0, len(rows)):
        fields.append(rows[i])
    df_result.columns = fields

    df_result = df_result.iloc[2:]
    for col in df_result.columns:
        if col != 'Date':
            df_result[col] = pd.to_numeric(df_result[col],errors='ignore')
    return df_result