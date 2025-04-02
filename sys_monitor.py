import os
import psutil
import socket
import time
import shutil

# Function to check internet connectivity
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return "Online"
    except OSError:
        return "Offline"

# Function to get system resource usage
def get_system_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    return {
        "CPU Usage": f"{cpu_usage}%",
        "RAM Usage": f"{ram_usage}%",
        "Disk Usage": f"{disk_usage}%",
    }

# Function to generate a full system report
def generate_report():
    stats = get_system_stats()
    internet_status = check_internet()

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    report = f"System Report ({timestamp})\n" + "-"*40 + "\n"
    
    for key, value in stats.items():
        report += f"{key}: {value}\n"
    report += f"Internet Status: {internet_status}\n"

    with open("system_report.log", "a") as log_file:
        log_file.write(report + "\n")
    
    print(report)
    print("Report saved to system_report.log")

# Function to clean temporary files
def clean_temp_files():
    temp_dir = os.getenv('TEMP')  # Get the temp folder path
    if not temp_dir or not os.path.exists(temp_dir):
        print("\nError: Temp folder not found!")
        return

    try:
        file_count = 0
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    file_count += 1
                except Exception as e:
                    pass  # Ignore errors on locked files
        
        print(f"\nTemporary files cleaned! {file_count} files deleted.")
    except Exception as e:
        print(f"\nError cleaning temp files: {e}")

# Main interactive loop
while True:
    print("\n=====================================")
    print("        SYSTEM MAINTENANCE TOOLKIT")
    print("=====================================")
    print("1. Monitor CPU, RAM, and Disk Usage")
    print("2. Check Internet Connectivity")
    print("3. Generate a Full System Report")
    print("4. Clean Temporary Files")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ").strip()

    if choice == "1":
        stats = get_system_stats()
        print("\nSystem Resource Usage:")
        for key, value in stats.items():
            print(f"{key}: {value}")
    elif choice == "2":
        status = check_internet()
        print(f"\nInternet Connectivity: {status}")
    elif choice == "3":
        generate_report()
    elif choice == "4":
        clean_temp_files()
    elif choice == "5":
        print("\nExiting the System Maintenance Toolkit. Goodbye!")
        break
    else:
        print("\nInvalid option! Please enter a valid choice.")
