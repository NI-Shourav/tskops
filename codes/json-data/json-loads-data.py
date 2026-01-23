import json

# 1. This is a STRING (notice the triple quotes). 
# It looks like a dictionary, but Python sees it as text.
raw_api_response = """
{
    "status": "success",
    "data": {
        "instance_id": "i-0abc123def",
        "state": "running"
    }
}
"""

# 2. Use json.loads() to turn that string into a Python Dictionary
data = json.loads(raw_api_response)

# 3. Now you can use it in your automation logic
if data["status"] == "success":
    print(f"Cloud Instance {data['data']['instance_id']} is {data['data']['state']}.")
else:
    print("API call failed!")