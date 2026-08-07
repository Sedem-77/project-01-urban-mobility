"""
data_ingestion.py

A reusable Python module for loading data from various file formats into a Pandas DataFrame.
"""

def load_data(file_path: str):#-> pd.Dataframe:
    """
    Here, we are defining a function called load data that takes file paths and load them into a pandas dataframe ( ->pd.DataFrame: is to specify it loads them into pandas dataframe)
    Parameters:
    - file_path (str): The path to the data file. it must be a string. example: "data/raw/yellow_tripdata_2026-01.parquet"
    - Our function will support extensions such as .csv, .xlsx, .parquet, and .json

    Returns:
    - pd.DataFrame: A DataFrame containing the loaded data.
    
    """
    import os 
    import pandas as pd 


    # Check if the fule exist

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Determine the file extenstion type and load accordingly

    root, file_extension = os.path.splitext(file_path) #this split the file path into the root and the file extension. example: "data/raw/yellow_tripdata_2026-01.parquet" will be split into "data/raw/yellow_tripdata_2026-01" and ".parquet"

    if file_extension == ".csv":
        return pd.read_csv(file_path)
    elif file_extension == ".xlsx":
        return pd.read_excel(file_path)
    elif file_extension == ".parquet":
        return pd.read_parquet(file_path)
    elif file_extension == ".json":
        return pd.read_json(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}. Supported formats are .csv, .xlsx, .parquet, and .json.")
        
