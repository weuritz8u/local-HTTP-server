# script written by Shadowdara

import os
import sys

import http.server
import socketserver

import tkinter as tk
from tkinter import filedialog

import socket

# vars
vdo_print = True

# functions

# for printing disableling
def do_print(text):
    if vdo_print:
        print(text)

# check the port
def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) == 0

# start the server
def start_server(PORT):
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        do_print("\nhttps://github.com/weuritz8u/local-HTTP-Server\nthe source repository with more information and guides\n")
        do_print(f"server path: {folder_path}\n")
        do_print(f"server runs on http://localhost:{PORT}\n")
        do_print("The Server runs forever now!\n")
        httpd.serve_forever()

# run on execution
try:
    argh_1 = int(sys.argv[1])

    if argh_1 >= 1:
        argh_1 -= 1
        vdo_print = False

except:
    pass

do_print("\nTerminal Output is set to true!")

try:
    if len(sys.argv) > 2:
        if sys.argv[2] == '$$1':
            folder_path = os.getcwd()

        elif sys.argv[2] == '$$0':
            raise NameError

        else:
            try:
                os.chdir(sys.argv[2])
                folder_path = os.getcwd()

            except:
                do_print("Error: Could not switch to the directory!")
                raise NameError
    else:
        raise NameError

except:
    try:
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory(title="Select the root folder for the server!")

        if not folder_path:
            raise ValueError("No Folder Selected!")

        os.chdir(folder_path)

    except Exception as e:
        do_print(f"Error: {e}")
        sys.exit(8)


do_print("\nSimple HTTP Server script by Shadowdara\n")

try:
    PORT = int(sys.argv[3])

    start_server(PORT)

except:
    do_print("Argv 3 not usable as Port!")

    PORT = 8000

    while PORT <= 49140:
        if is_port_in_use(PORT):
            do_print(f"Port {PORT} is busy, trying {PORT+1}")
            PORT += 1

        else:
            break

    if PORT > 49140:
        do_print("Kein freier Port gefunden, Server kann nicht gestartet werden!")
        sys.exit(1)

    try:
        start_server(PORT)

    except:
        do_print(f"Port {PORT} is busy")
        sys.exit(1)
