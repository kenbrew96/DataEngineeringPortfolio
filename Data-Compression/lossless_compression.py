import gzip

def compress_data(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            f_out.writelines(f_in)

if __name__ == '__main__':
    compress_data('data/input.txt', 'data/output.gz')

