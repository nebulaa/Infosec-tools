# Check the HTTP response code and response history by sending a GET request
# Input requires a .txt file with URLs such as http://example.com in every line

import requests
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("input_path", type=str)
args = parser.parse_args()

def run(input_path):
    
    with open(input_path, 'r') as f:
        links = f.read().splitlines()

        for link in tqdm(links):
            try:
                response = requests.get(link, timeout=5)
                print (link, "returns", response.status_code, response.history)
            except:
                print(link, "returns nothing")

if __name__ == "__main__":
    run(
        input_path = args.input_path,
    )