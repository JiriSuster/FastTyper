import os

def start():
    port = 62159
    os.system(f"start \"\" http://www.localhost:{port}/game_mode.html")
    os.system(f'cmd /c "start /min python -m http.server {port}"')# /c kills console after stopping server, /min makes the console minimized

if __name__ == "__main__":
    start()
