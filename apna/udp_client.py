import socket

def send_file(file_path, host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except Exception as e:
        print(f"Error creating socket: {e}")
        return

    try:
        with open(file_path, 'rb') as file:
            print(f"Sending {file_path} to {host}:{port}...")
            while True:
                data = file.read(4096)  # Read in larger chunks for efficiency
                if not data:
                    break
                s.sendto(data, (host, port))
        # Send an empty packet to indicate end of file transfer
        s.sendto(b'', (host, port))
        print(f"{file_path} sent successfully.\n")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"Error sending file: {e}")
    finally:
        s.close()

def main():
    # Define receiver details
    receiver_host = input("Enter the receiver's IP address or hostname: ")
    receiver_port_input = input("Enter the receiver's port (e.g., 5005): ")

    # Validate and convert port number
    try:
        receiver_port = int(receiver_port_input)
        if not (1024 < receiver_port < 65535):
            print("Please enter a port number between 1025 and 65534.")
            return
    except ValueError:
        print("Invalid port number.")
        return

    # Dictionary to map choices to file paths
    file_paths = {
        "1": "script.txt",
        "2": "audio.mp3",
        "3": "video.ts"
    }

    while True:
        # Prompt client user to choose which file to send next
        print("\nChoose the file type to send:")
        print("1. Script")
        print("2. Audio")
        print("3. Video")
        print("4. Exit")
        ch = input("Enter choice (1-4): ")

        if ch == '4':
            print("Exiting the client.")
            break

        if ch not in file_paths:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")
            continue

        file_path = file_paths[ch]
        send_file(file_path, receiver_host, receiver_port)

if __name__ == "__main__":
    main()
