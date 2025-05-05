import os
import webbrowser
import platform

def start():
    port = 62159
    if (platform.system() == "Windows"):
        os.system(f"start \"\" http://www.localhost:{port}/game_mode.html")

        # /c kills console after stopping server, /min makes the console minimized
        os.system(f'cmd /c "start /min python -m http.server {port}"')
    else:
        webbrowser.open(f"http://localhost:{port}/game_mode.html")
        os.system(f'nohup python3 -m http.server {port} >/dev/null 2>&1 &')

if __name__ == "__main__":
    start()
