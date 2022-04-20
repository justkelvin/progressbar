#!/usr/bin/env python3

# Imports
from tqdm import tqdm
import requests

url = "http://127.0.0.1:8000/myfile.pdf"
file_name = "myfile.pdf"
chunk_size = 1024
r = requests.get(url, stream=True)
file_size = int(r.headers["content-length"])

with open(file_name, "wb") as f:
    for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=file_size/chunk_size, unit="KB"):
        f.write(data)
print("Download complete")