import json
import sys

def parse_vlans(filename):

  try:
    with open(filename) as f:
      data = json.load(f)
  
  except json.JSONDecodeError:
    print(f"Error parsing {filename} as JSON")
    return None

  vlan_ids = set()
  
  for item in data.get("items", []): 
    vlan_id = item.get("vn_instance", {}).get("vlan_id")
    if vlan_id:
      vlan_ids.add(int(vlan_id))

  if not vlan_ids:
    return None

  return list(vlan_ids)

def print_results(filename, vlans):

  if not vlans:
    print(f"No VLANs found in {filename}")
    return

  print(f"VLANs from {filename}:")
  print(vlans)
  print(f"Count: {len(vlans)}")

file1 = "rz.json"
file2 = "vlans.json"

vlans1 = parse_vlans(file1)
print_results(file1, vlans1)

vlans2 = parse_vlans(file2)
print_results(file2, vlans2)