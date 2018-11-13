import argparse
import sys

def create_parser():
    '''
    Function to create the parser. It will check that the file exists if importing before continuing 
    and if called with the --export flag will check that the file can be written to 
    '''
    parser = argparse.ArgumentParser(description="hrTool will import a list of users and manipulate the local users on the system to match the json file")
    parser.add_argument("jsonfile",
        help="This file will be read from, unless the --export flag is specified, in which case it is written to",
        type=str)
    parser.add_argument("--export","-e",
        help="exports user configuration to a specified file",
        action='store_const',
        const=True,
        default=False)
    #args = parser.parse_args()
    
    # if args.export == False:
    #     try:
    #         with open(args.jsonfile,'r') as f:
    #             return parser
                
    #     except FileNotFoundError as err:
    #         print(f"File does not exist, please check the location and try again")
    #         print(f"{err}")
    #         sys.exit(1)
    #     except OSError as err:
    #         print("Some other error has happend! Please review your input")
    #         print(f"{err}")
    #         sys.exit(3)
        # finally:
        #     return parser
    return parser