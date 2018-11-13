import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="hrTool will import a list of users and manipulate the local users on the system to match the json file")
    parser.add_argument("jsonfile",
        help="This file will be read from, unless the --export flag is specified, in which case it is written to",
        required=True)
    parser.add_argument("--export","-e",
        help="exports user configuration to a specified file",
        action='store_const',
        const=True,
        default=False)
    return parser