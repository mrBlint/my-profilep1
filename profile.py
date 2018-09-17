"""This is a description of your profile, it can be multi-line.
Every profile must include a description. 

Instructions:
These are instructions for using your profile after it is instantiated.
Instructions are optional.
"""	
# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.
node1 = request.XenVM("node1")

node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"

node1.routable_control_ip = "true"


# Install and execute a script that is contained in the repository.
node1.addService(pg.Execute(shell="/bin/sh", command="sudo local/repository/silly.sh"))
# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
