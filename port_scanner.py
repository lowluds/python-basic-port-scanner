#project# port scanner
import socket, time

timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"port_scan_{timestamp}.txt"

print("=== Python Port Scanner ===")

# Get target IP
try:
    target = input("Enter target IP (e.g., 127.0.0.1): ")
except:
    print("Invalid input! Please enter the correct IP.")

# Start scanning from port
while True:
    try:
        start_port = int(input("Enter starting port number to scan: "))
        if start_port < 1:
            print("Ports must be greater than 0.")
        else:
            break
    except:
        print("Invalid input! Please enter the correct port.")

# End scanning at port
while True:
    try:
        end_port = int(input("Enter the ending port number to scan: "))
        if end_port > 65535:
            print("Ports must be between 1 and 65535.")
        elif start_port >= end_port:
            print("Starting port must be lower than ending port.")
        else:
            break
    except:
        print("Invalid input! Please enter the correct port.")

file = open(filename, "w") 

# Create socket and scan
scan_start_time = time.time()

print(f"Target: {target}")
print(f"Scanning ports {start_port} to {end_port}\n")

for port in range(start_port, end_port):
    print(f"Scanning port {port}...")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))  # this checks the port
    sock.close()

    if result == 0:
        print("Port", port, "is open.")
        file.write(f"Port {port} is open.\n")
    else:
        print("Port", port, "is closed.")
        file.write(f"Port {port} is closed.\n")

scan_end_time = time.time()

#print("Scan completed in", scan_end_time - scan_start_time, "seconds")
print(f"Scan completed in {scan_end_time - scan_start_time:.2f} seconds")

file.close()