# Script to run whois lookup on a list of IPs
# Requires an input.txt file with a list of IPs and the name of an output file such as output.csv
# Output file will be in .csv format

from ipwhois import IPWhois
import csv
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("input_path", type=str)
parser.add_argument("output_path", type=str)
args = parser.parse_args()


def run(input_path, output_path):
    
    with open(input_path, 'r') as f:
        links = f.read().splitlines()
    
    
    with open(output_path, 'w+', newline='') as o:
        fieldnames = ['url', 'asn', 'asn_cidr', 'asn_contry_code','asn_date', 'asn_registry', 'asn_address', 'asn_cidr','asn_city', 'asn_country', 'created', 'asn_description', 'asn_emails', 'asn_range', 'error']
        writer = csv.DictWriter(o, fieldnames=fieldnames)
        writer.writeheader()
        for link in tqdm(links):
            try:
                obj = IPWhois(link)
                res = obj.lookup_whois()
                writer.writerow(
                    {
                        fieldnames[0]: link,
                        fieldnames[1]: res["asn"],
                        fieldnames[2]: res["asn_cidr"],
                        fieldnames[3]: res["asn_country_code"],
                        fieldnames[4]: res["asn_date"],
                        fieldnames[5]: res["asn_registry"],
                        fieldnames[6]: res["nets"][0]['address'],
                        fieldnames[7]: res["nets"][0]['cidr'],
                        fieldnames[8]: res["nets"][0]['city'],
                        fieldnames[9]: res["nets"][0]['country'],
                        fieldnames[10]: res["nets"][0]['created'],
                        fieldnames[11]: res["nets"][0]['description'],
                        fieldnames[12]: res["nets"][0]['emails'],
                        fieldnames[13]: res["nets"][0]['range'],

                    }
                     )
            except:
                print(f"Something else went wrong...")
                writer.writerow(
                    {
                        fieldnames[0]: link,
                        fieldnames[14]: (f"timeout or other error")
                    }
                )
if __name__ == "__main__":
    run(
        input_path = args.input_path,
        output_path = args.output_path
    )