# script written by Shadowdara

import subprocess

# vars
script_path = 'addons/create_http_server.py'
folder_path = '$$0'

# run on execution
print("starting local HTTP Server by Shadowdara\n")

port = input("Type your fav port [or just hit enter]: ")

try:
    subprocess.run(['python', script_path, "0", folder_path, port])

except:
    print("\nError\nCould not start the server")
    input("... ")
