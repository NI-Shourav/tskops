from datetime import datetime

file_name = 'error.log'

timestamp = datetime.now().strftime("%Y%m%d_%H%M%s")

new_file_name = f"{file_name}_{timestamp}.bac"

print(new_file_name)

