import requests

def collect_telemetry_data():
    response = requests.get('http://example.com/api/data')
    data = response.json()
    return data

if __name__ == '__main__':
    telemetry_data = collect_telemetry_data()
    print(telemetry_data)

