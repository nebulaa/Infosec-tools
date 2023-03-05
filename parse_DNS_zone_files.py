#requires zonefile.txt as input

import zonefile_parser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_path", type=str)
args = parser.parse_args()


def run(input_path):
    
    with open(input_path, 'r') as stream:
        content = stream.read()
        records = zonefile_parser.parse(content)

        for record in records:
            print(record.rtype, record.name)
    
if __name__ == "__main__":
    run(
        input_path = args.input_path,
    )