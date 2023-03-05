#input needs to be a .txt file with a list of sites such as https://test.abc.com

import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_path", type=str)
args = parser.parse_args()

def run(input_path):
    
    with open(input_path, 'r') as f:
        links = f.read().splitlines()

        for link in links:
            try:
                reqs = requests.get(link, timeout=4)
                soup = BeautifulSoup(reqs.text, 'html.parser')
                for title in soup.find_all('title'):
                    print(link,",",title.get_text())
            except:
                print(link, "returns nothing")

if __name__ == "__main__":
    run(
        input_path = args.input_path,
    )
