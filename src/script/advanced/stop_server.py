import mcrcon
import time

# using minecraft's rcon port feature to close/stop server remotely
# why not use RCON to start server? Too complicated for my tiny brain.

def stop_server():
    try:
        # replace this with actual information (localhost=x.x.x.x)
        host = 'localhost'
        port = 25575
        password = 'root_admin'

        with mcrcon.MCRcon(host, password, port) as mc:
            response = mc.command('stop')
            print(response)
    except mcrcon.MCRconException as e:
        print(f"Error: {e}")

time.sleep(10)

stop_server()
