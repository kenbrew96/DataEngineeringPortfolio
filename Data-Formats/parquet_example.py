import pandas as pd

def read_parquet():
    data = pd.read_parquet('data/input.parquet')
    return data

if __name__ == '__main__':
    data = read_parquet()
    print(data)

