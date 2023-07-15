# checks MD5 hash of a distributed binary against a given hash
# includes a simple textual loading bar

import hashlib
import os
from tqdm import tqdm
# pip install tqdm

def calculate_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        file_size = os.path.getsize(file_path)
        chunk_size = 4096
        with tqdm(total=file_size, unit='B', unit_scale=True, desc=file_path.split('/')[-1]) as pbar:
            for block in iter(lambda: file.read(chunk_size), b''):
                hasher.update(block)
                pbar.update(len(block))
    return hasher.hexdigest()

def check_md5():
    file_path = input("Enter the file path: ")
    expected_md5 = input("Enter the expected MD5 hash: ")
    calculated_md5 = calculate_md5(file_path)
    if calculated_md5 != expected_md5:
        print(f'MD5 mismatch: got {calculated_md5}, expected {expected_md5}')
    else:
        print('MD5 match.')

check_md5()
