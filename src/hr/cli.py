import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="hrTool will import a list of users and manipulate the local users on the system to match the json file")
    parser.add_argument("jsonfile",
    help="This file will be read from, unless the --export flag is specified, in which case it is written to",
    required=True)
