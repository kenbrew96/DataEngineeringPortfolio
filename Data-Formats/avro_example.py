import fastavro
from fastavro import reader

def read_avro():
    with open('data/input.avro', 'rb') as f:
        avro_reader = reader(f)
        for record in avro_reader:
            print(record)

if __name__ == '__main__':
    read_avro()

