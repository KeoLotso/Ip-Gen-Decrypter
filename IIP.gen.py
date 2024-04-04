import os
import random

def generate_ip():
    ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))
    return ip

def main():
    ips = []
    file_path = os.path.join(os.path.dirname(__file__), "Ips.txt")

    # Check if file already exists
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if not file_exists:
            file.write("Generated IP addresses:\n")

    while True:
        ip = generate_ip()
        print("Generated IP address:", ip)
        ips.append(ip)
        
        with open(file_path, "a") as file:
            if len(ips) > 1:
                file.write(ip + "\n")
            else:
                file.write(ip + "\n\n")
        
        try:
            input_timeout = input("Press Enter to generate another IP address (or type 'exit' to stop): ")
            if input_timeout.lower() == 'exit':
                break
        except KeyboardInterrupt:
            break
    
    print(f"{len(ips)} IP addresses generated and saved to Ips.txt.")

if __name__ == "__main__":
    main()
