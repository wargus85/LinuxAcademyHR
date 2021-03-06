import argparse, os

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
        
    return parser

def main():
    import json, os, sys
    from hrtool import parsejson, usermod
    
    if os.geteuid() !=0:
        print(f"please try again, as super user (sudo)")
        sys.exit(1)

    arguments = create_parser().parse_args()

    if arguments.export == False:
        with open(arguments.jsonfile,'r') as f:
            for line in f.readline():
                json_user = json.loads(line.replace("\'", "\""))
                if json_user["delete"] == True:
                    usermod.del_user(json_user["name"],delete=True)
                else:
                    usermod.mod_user(json_user["name"],json_user["groups"],json_user["password"])
    else:
        parsejson.writefile(arguments.jsonfile)
