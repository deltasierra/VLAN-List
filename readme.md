## Overview

How to get a list and count all of the VLANs assigned in your blueprint under Apstra.

## Leaf VLANs Graph Query

1. In Apstra, navigate to `platform > developer > graph-explorer.`
2. Select the desired Blueprint in the dropdown.
3. Enter the following graph query and then click the Execute button. 

`node('vn_instance', name='vn_instance')`

## Save the returned data

1. Copy the returned data and paste it into the vlans.json file.

## Routing Zone (RZ) Graph Query

In addition, you can query the graph to get a list of all of the Routing Zones configured, along with the VLAN IDs assigned to each RZ.

1. Enter the following graph query and then click the Execute button.

`node('security_zone', name='vn_instance')`

## Save the returned data

1. Copy the returned data and paste it into the rz.json file.

## Run the script

1. Click the `Run` button above.