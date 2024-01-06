# Import Modules
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import Resources
#import lookupAADGroup
#import readInUserGroupsFromExcel


# Set up Azure credentials
credential = DefaultAzureCredential()

# Create a resource management client
resource_client = Resources(credential)


