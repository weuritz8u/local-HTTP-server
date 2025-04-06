# script written by Shadowdara

import os
import subprocess

# vars
script_path = 'addons/create_http_server.py'
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), script_path)

# run on execution
print("starting local HTTP Server by Shadowdara\n")

try:
    subprocess.run(['python', path])

except:
    print("\nError\nCould not start the server")
    input("... ")
