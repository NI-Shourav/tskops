# DevOps Python Homework: The Automation Specialist

**Instructions:** Fork this repository and create 10 folders/directories for 10 tasks. There will be 2 files per folder, for example:

Python-DevOps-Homework/

    ├── Task_01_Domain_Extractor/

        ├── Problem_01.txt

        └── solution_01.py

Once it is done, push it to a separate GitHub repository for future use

--------
### Task 1: The Domain Extractor (Slicing & Strings)

**Scenario:** You have a list of web URLs. 

**Goal:** Create a script that takes the URL `https://api.github.com/v3` and uses **slicing** or `.split()` to extract just the domain name (`github.com`). 

**DevOps Value with this task:** Parsing logs to see which external services your app is calling.

### Task 2: The "Safe Name" Sanitizer (Strings)

**Scenario:** A user wants to create a cloud bucket named `My Project Backup` . Cloud providers don't allow spaces or uppercase. 

**Goal:** Use string methods to: 
1. Strip whitespace. 
2. Replace spaces with hyphens. 
3. Convert to lowercase. 

**DevOps Value with this task:** Standardizing resource names in Terraform/Cloud scripts.

### Task 3: The Port Validator (Integers & Logic)

**Scenario:** A firewall script receives a port as a string `"8080"`. 

**Goal:** Convert the string to an integer and check if it is within the valid range (1–65535). Print "Valid" or "Invalid". 

**DevOps Value with this task:** Input validation for automation tools.

### Task 4: The Fleet Inventory (Lists)

**Scenario:** You have a list: `servers = ["web01", "db01", "app01", "web02"]`. 

**Goal:** Use **slicing** to create a new list called `web_servers` containing only the first and last elements of the original list. 

**DevOps Value with this task:** Managing subsets of infrastructure (e.g., "only update the first 50% of nodes").

### Task 5: The Cloud Config Mapper (Dictionaries)

**Scenario:** Create a dictionary representing a Virtual Machine with keys: `id`, `ip`, `status`, and `region`. 

**Goal:** Write a script that updates the `status` from `"running"` to `"stopped"` and adds a new key called `instance_type` with the value `"t3.large"`. 

**DevOps Value with this task::** Mimicking JSON responses from AWS/Azure/GCP APIs.

### Task 6: The Log File Duplicator (OS & Shutil)

**Scenario:** You need to test a new log-parsing script without ruining the original files. 

**Goal:** Write a script that looks for a file named `app.log` and creates 5 copies of it named `app_1.log`, `app_2.log`, etc. 

**DevOps Value with this task::** Generating "mock data" for testing pipelines.

### Task 7: The "Prod" Guard (Booleans & Conditionals)

**Scenario:** A script is about to delete data. 

**Goal:** Create a variable `env = "production"`. Write an `if` statement that only prints "Executing Delete" if `env` is NOT equal to "production". Otherwise, print "Access Denied: Cannot delete in Prod!" 

**DevOps Value with this task::** Implementing safety "gates" in CI/CD pipelines.

### Task 8: The Threshold Alert (Floats & Strings)

**Scenario:** Your monitoring tool returns a CPU load of `0.88`. 

**Goal:** Format this float as a percentage string (e.g., `"88%"`) using **f-strings**. 

**DevOps Value with this task:** Creating human-readable alerts for Slack or Email.

### Task 9: The Path Builder (Pathlib/OS)

**Scenario:** You are working on a script that must run on both Windows and Linux. 

**Goal:** Use `os.path.join` to combine the variables `base_dir = "/var/log"`, `app_name = "nginx"`, and `filename = "access.log"` into one valid path. 

**DevOps Value with this task:** Avoiding "Hardcoded Path" bugs.

### Task 10: The Secret Masker (Slicing)

**Scenario:** You accidentally printed an API Key to the console: `AKIA1234567890EXAMPLE`. 

**Goal:** Use slicing to print only the first 4 characters followed by asterisks (e.g., `AKIA**********`). 

**DevOps Value with this task:** Security and compliance in logging.

---------CHEERS!--------