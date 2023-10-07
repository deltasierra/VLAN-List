import json
import sys

# Define a function to parse a JSON file and extract VLAN IDs
def parse_vlans(filename):

    # Try to open the file and load its contents as JSON
    try:
        with open(filename) as f:
            data = json.load(f)
    
    # If there is an error parsing the JSON, print an error message and return None
    except json.JSONDecodeError:
        print(f"Error parsing {filename} as JSON")
        return None

    # Create an empty set to store the VLAN IDs
    vlan_ids = set()
    
    # Iterate over each item in the JSON data
    for item in data.get("items", []): 
        # Get the VLAN ID from the current item
        vlan_id = item.get("vn_instance", {}).get("vlan_id")
        
        # If the VLAN ID exists, add it to the set of VLAN IDs
        if vlan_id:
            vlan_ids.add(int(vlan_id))

    # If no VLAN IDs were found, return None
    if not vlan_ids:
        return None

    # Return the list of VLAN IDs
    return list(vlan_ids)

# Define a function to print the results of the VLAN extraction
def print_results(filename, vlans):

    # If no VLANs were found, print an error message and return
    if not vlans:
        print(f"No VLANs found in {filename}")
        return

    # Print the filename and the list of VLANs
    print(f"VLANs from {filename}:")
    print(vlans)
    print(f"Count: {len(vlans)}")

# Call the functions to parse the JSON files and print the results
file1 = "rz.json"
file2 = "vlans.json"

vlans1 = parse_vlans(file1)
print_results(file1, vlans1)

vlans2 = parse_vlans(file2)
print_results(file2, vlans2)