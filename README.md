# Infosec Tools for Information Gathering

This repository contains a collection of Python scripts and tools designed to assist in information gathering for Infosec purposes. These tools are aimed at helping security professionals and researchers in various aspects of information gathering and analysis.

## Tools Overview

### check_mTLS_authentication

This tool utilizes Curl commands to connect to target servers and identify if a client certificate is requested for mutual TLS (mTLS) authentication. It takes input in the form of a `.txt` file containing a list of target servers and produces an output in a `.csv` file format.

### find_ip_using_url

The `find_ip_using_url` tool is designed to find the corresponding server IP addresses for a given list of websites. It reads input from a `.txt` file and provides the IP address information as output.

### HTTP_Response_Checker

This tool helps track and monitor HTTP response codes from a list of specified URLs. It takes a `.txt` file as input, containing the list of URLs to monitor, and provides information on the HTTP response codes returned by these URLs.

### parse_DNS_zone_files

The `parse_DNS_zone_files` tool is designed to extract various DNS records (A, AAAA, CNAME, MX, etc.) from a given DNS zone file. You can input a DNS zone file in `.txt` format, and the tool will parse it and present the extracted DNS records.

### Parse_Website_title

This tool extracts the title HTML tags from websites using the Beautiful Soup module. You can input a list of URLs in a `.txt` file, and the tool will extract and present the titles of the web pages.

### pywappalyzer

`pywappalyzer` is a command-line interface (CLI) implementation of Wappalyzer using Python libraries. It can be used to analyze web applications and identify the technologies used in their development. Input is provided in the form of a `.txt` file containing URLs to analyze.

### whois_lookup_with_IP

This tool performs a WHOIS lookup on a list of IP addresses. You can input a list of IP addresses in a `.txt` file, and the tool will perform WHOIS queries and present the results in a `.csv` file format.

These Infosec tools are designed to streamline the information gathering process and provide valuable insights for security assessments and research. Feel free to explore and use these tools as needed for your Infosec tasks.
