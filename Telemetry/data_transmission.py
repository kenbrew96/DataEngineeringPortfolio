import requests

def transmit_telemetry_data(data):
    response = requests.post('http://example.com/api/telemetry', json=data)
    print(f"Data transmitted: {response.status_code}")

if __name__ == '__main__':
    telemetry_data = {"temperature": 23.5}
    transmit_telemetry_data(telemetry_data)

