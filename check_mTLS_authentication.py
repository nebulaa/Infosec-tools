# Script to verify if mutual TLS authentication is required to connect to the webserver
# Requires an input.txt file with a list of URLs such as https://example.abc.com and the name of an output file such as output.csv
# Output file will be in .csv format

import subprocess
import csv
import argparse
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument("input_path", type=str)
parser.add_argument("output_path", type=str)
args = parser.parse_args()


def run1(input_path, output_path):
    
    with open(input_path, 'r') as f:
        links = f.read().splitlines()
    
    with open(output_path, 'w+', newline='') as o:
        fieldnames = ['url', 'output', 'error', 'except']
        writer = csv.DictWriter(o, fieldnames=fieldnames)
        writer.writeheader()
        for link in tqdm(links):
            try:
                writer = csv.DictWriter(o, fieldnames=fieldnames)
                sh_response = subprocess.run(["curl", "-s", "-S", "-L", "-I", link], capture_output=True, text=True, timeout=5)
                writer.writerow(
                    {
                        fieldnames[0]: link,
                        fieldnames[1]: sh_response.stdout,
                        fieldnames[2]: sh_response.stderr,
                    }
                )
            except:
                print(f"Something else went wrong...")
                writer.writerow(
                    {
                        fieldnames[0]: link,
                        fieldnames[3]: (f"timeout or other error")
                    }
                )
if __name__ == "__main__":
    run1(
        input_path = args.input_path,
        output_path = args.output_path
    )