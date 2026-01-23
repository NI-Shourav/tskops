import json

# 1. Open the file in read mode ('r')
try:
    with open('config.json', 'r') as file:
        # 2. Parse JSON into a Python Dictionary
        config_data = json.load(file)

    # 3. Access the data like a normal Dictionary
    print(f"--- System Report for {config_data['server_name']} ---")
    print(f"IP: {config_data['ip_address']}")
    
    # 4. Accessing the list inside the JSON
    print("Running Services:")
    for service in config_data['services']:
        print(f"  - {service}")

except FileNotFoundError:
    print("Error: config.json file not found!")
except json.JSONDecodeError:
    print("Error: Failed to parse JSON. Check for syntax errors (commas, quotes).")