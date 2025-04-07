# local-HTTP-server

## How to

easy create a local HTTP server for debugging HTML Websites with a python script

run `server_start.py` to start the server with python

## Dev Info

*These infos are only needed when you want to use the script anywhere else and run it directly without the `server_start.py`*

**The Server will be started with 3 arguments**

- argv[1] =
    - `1` -> no text output in the terminal
    - `0` -> text output in the terminal

- argv[2] =
    - `$$0` -> select the folder in popup window
    - `$$1` -> use the `path` where the script is executed
    - `*(any input)*` -> try to use the input as folder path, when it dont work, must be selected via a popup window

- argv[3]
    - This is the used `PORT`, if the port doesn't work, the script will autmaticly search another one

**when running the script without arguments**

- argv[1] -> text output in the terminal
- argv[2] -> popup window to select the folder
- argv[3] -> PORT = `8000`, but the script will search for another one when `8000` is busy

## Contribute

*feel free to contribute and fork this Repository*

*LICENSE*: MIT
