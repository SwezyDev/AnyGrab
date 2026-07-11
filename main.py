from rgbprint import gradient_print, gradient_scroll, Color
import subprocess
import ctypes
import psutil
import time
import os

BLACKLIST = set() # Persistent global blacklist to avoid duplicate entries

class utility:
    logo = """                              
                █████       ██████                              
             ███████████      ██████                            
           ████████████████      ███████                         
        █████████████████████      ██████                      
      █████████████████████████       ██████       Against Indian Scammers
    █████████████████████████████       ██████     Coded by Swezy <3
      █████████████████████████       ██████                     
         ███████████████████       ██████                       
           ███████████████       ██████                          
              █████████       ██████                            
                █████       █████         
""" # Logo

    def console_transparency():
        percentage = 10 # Set the transparency level (0-100)
        hwnd = ctypes.windll.kernel32.GetConsoleWindow() # Get the console window handle
        styles = ctypes.windll.user32.GetWindowLongW(hwnd, -20) # Get the current window styles
        styles |= 0x80000 # Add the layered style
        ctypes.windll.user32.SetWindowLongW(hwnd, -20, styles) # Set the new window styles
        ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, int(255 * (100 - percentage) / 100), 2) # Set the transparency

    def find_anydesk():
        pids = []
        for p in psutil.process_iter(["pid", "name"]): # Iterate over all processes
            if "anydesk" in p.info["name"].lower(): # Check if the process name contains "anydesk"
                pids.append(p.info["pid"]) # Add the PID to the list
        return pids # Return the list of AnyDesk PIDs

def grab(anydesk_pid):
    gradient_print(f"[#] AnyGrab is Connected! --> {anydesk_pid}", start_color=Color.ghost_white, end_color=Color.sky_blue) # Print running message

    while True: # Infinite loop to monitor AnyDesk connections
        try: # Try block to handle exceptions
            anydesk_pids = utility.find_anydesk() # Find AnyDesk PIDs
            anydesk_addy = {} # Reset AnyDesk addresses

            for con in psutil.net_connections(kind="tcp"): # Iterate over all TCP connections
                if con.pid not in anydesk_pids: # Check if the connection belongs to AnyDesk
                    continue # Continue to the next connection
                if con.status == psutil.CONN_LISTEN: # Check if the socket is listening
                    continue # Continue to the next connection
                if not con.raddr: # Check if the remote address is valid
                    continue # Continue to the next connection

                ip_, port_ = con.raddr.ip, con.raddr.port # Split the remote address into IP and port
                anydesk_addy[ip_] = port_ # Store the IP and port in the dictionary

            for ip, port in anydesk_addy.items(): # Iterate over the AnyDesk addresses
                if not ip.startswith("169.254.") and not ip == "127.0.0.1" and port not in [80, 443] and ip not in BLACKLIST: # Ignore local link addresses and check blacklist
                    gradient_print(f" [!] {ip}:{port}", start_color=Color.ghost_white, end_color=Color.sky_blue) # Print the address
                    BLACKLIST.add(ip) # Add the address to the blacklist

        except Exception: # Handle exceptions
            continue # Continue to the next iteration


def main():
    os.system("mode 83,30" if os.name == "nt" else "printf '\e[8;30;83t'") # Set console size
    
    while True:
        os.system("cls" if os.name == "nt" else "clear") # Clear the console
        gradient_print(utility.logo, start_color=Color.ghost_white, end_color=Color.sky_blue) # Print the logo
        gradient_scroll("[+] Waiting for AnyDesk", start_color=Color.ghost_white, end_color=Color.violet) # Print waiting message

        pid = utility.find_anydesk() # Find AnyDesk PID
        
        if pid: # If AnyDesk is running
            anydesk_pid = pid[0] # Get the first PID
            grab(anydesk_pid) # Call the grab function

        time.sleep(1) # Sleep for 1 second before checking again


if __name__ == "__main__":
    utility.console_transparency() # Set console transparency
    main() # Call the main function
