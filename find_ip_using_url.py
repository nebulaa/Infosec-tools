#requires a .txt file with a list of URLs such as: example.org

import socket
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
                ip = socket.gethostbyname(link)
                print(f"IP address of {link} is {ip}")
            except:
                print(f"{link} cannot be resolved")

if __name__ == "__main__":
    run(
        input_path = args.input_path,
    )
