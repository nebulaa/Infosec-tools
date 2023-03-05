#Find the underlying technology stack of the website
#Wappalyzer is a technology profiler that shows you what websites are built with

from pywappalyzer import Pywappalyzer
import argparse
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument("input_path", type=str)
args = parser.parse_args()

wappalyzer = Pywappalyzer()

def run(input_path):
    
    with open(input_path, 'r') as f:
        links = f.read().splitlines()
        for link in tqdm(links):
            try:
                data = wappalyzer.analyze(url=link)
                print (link, "returns", data)
            except:
                print(link, "returns nothing")
    
if __name__ == "__main__":
    run(
        input_path = args.input_path,
    )