import pandas as pd

def read_csv():
    data = pd.read_csv('data/input.csv')
    return data

if __name__ == '__main__':
    data = read_csv()
    print(data)

