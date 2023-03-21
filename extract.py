import pandas as pd


def extract():
    """
    Extract data
    """
    CSV = 'https://raw.githubusercontent.com/jazzlyj/etl-pipeline-make-minikube-windows/main/DATASET.csv'
    COL_LIST = ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address']
    data = pd.read_csv(CSV, low_memory=True)
    df = pd.DataFrame(data, columns=COL_LIST)
    return df
