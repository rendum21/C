import socket
import os


def receive_file(port, base_dir="received_files"):
    # Create directory to store received files if it doesn’t exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Start listening on the given port
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("0.0.0.0", port))
    print(f"UDP Server is listening on port {port}...\n")

    file_count = 1  # For generating unique filenames

    while True:
        # Automatically generate a unique filename
        file_path = os.path.join(base_dir, f"received_file_{file_count}")
        print(f"Receiving file: {file_path}")

        with open(file_path, 'wb') as file:
            while True:
                # Receive data in chunks of 1024 bytes
                data, addr = s.recvfrom(65507)

                # Check if data is empty, indicating end of file transfer
                if not data:
                    print(f"File {file_path} received successfully.\n")
                    file_count += 1  # Increment file count for unique filenames
                    break

                # Write data to the file
                file.write(data)

    s.close()


if __name__ == "__main__":
    receiver_port = 1255  # Port for receiving files
    receive_file(receiver_port)
