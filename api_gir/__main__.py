import sys

from .init.init import copy_base_config
from .serve import server

def main():
    args = sys.argv[1:]

    try:
        command = args[0].lower()
        
        if command == "serve":
            print("GIR! Serve my software!")
            server.run_server()
        elif command == "build":
            print("GIR! Build my software!")
        elif command == "init":
            print("GIR! Init my project!")
            copy_base_config()
            print("FILE COPIED, SIR!")
        else:
            print("No command provided. Acceptable commands: build, init, serve")
    except:
        print('Could not complete your request. My head is full of pudding!')

if __name__ == "__main__":
    main()