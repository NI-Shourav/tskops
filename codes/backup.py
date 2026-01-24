import os
import shutil
from datetime import datetime

# The Scenario: Archive old log files
log_dir = "../logs"
archive_dir = "./archive"

# 1. Create directory if it doesn't exist
if not os.path.exists(archive_dir):
    os.makedirs(archive_dir)
    print(f"Created {archive_dir}")

# 2. Get a list of all files in the log directory
# os.listdir() returns a List
files = os.listdir(log_dir)

print(f"Found {len(files)} files in {log_dir}. Starting cleanup...")

# 3. Logic to move files using a loop
for file_name in files:
    # Check if the file ends with .log (String method practice!)
    if file_name.endswith(".log"):
        
        # Construct full file paths
        source_path = os.path.join(log_dir, file_name)
        destination_path = os.path.join(archive_dir, file_name)
        
        try:
            # Move the file (The DevOps Action)
            shutil.move(source_path, destination_path)
            print(f"✅ Archived: {file_name}")
        except Exception as e:
            print(f"❌ Failed to move {file_name}: {e}")

print("Cleanup complete.")


