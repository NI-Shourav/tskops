# app.py
import pymodules

# Scenario: Calculating server capacity or resource allocation
nodes = 10
processes_per_node = 4

# Using the multiply function from our module
total_capacity = pymodules.multiply(nodes, processes_per_node)

# Scenario: Dividing tasks across nodes
total_tasks = 43
tasks_per_node = pymodules.divide(total_tasks, nodes)
leftover_tasks = pymodules.remainder(total_tasks, nodes)

print(f"--- Infrastructure Report ---")
print(f"Total Capacity: {total_capacity} slots")
print(f"Tasks per Node: {tasks_per_node}")
print(f"Tasks remaining for manual queue: {leftover_tasks}")