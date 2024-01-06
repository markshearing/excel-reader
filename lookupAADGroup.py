from azure.mgmt.resource import ResourceManagementClient

#from azure.mgmt.resource import ResourceGroup

# Query Entra ID for each of the values in the group-name column to determine if they exist.
# If they do, output the Entra ID and the group-name value.
# If they don't, output the group-name value and the error message.

# Login to Microsoft Azure


def lookupAADGroup(group_name):

  print("hello")
  # Assuming you have a resource group named 'example-group'
  #group_name = 'example-group'

  # Query for the Entra ID for the resource group
  #resource_group = resource_client.resource_groups.get(group_name)
  #print(f"Entra ID for {group_name}: {resource_group.id}")
