import json

def read_json():
    with open('data/input.json', 'r') as file:
        data = json.load(file)
    return data

if __name__ == '__main__':
    data = read_json()
    print(data)

