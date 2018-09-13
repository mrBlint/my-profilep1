
# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.
node = request.XenVM("node")
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node.routable_control_ip = "true"
# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="/bin/sh", command="sudo yum -y install git"))
node.addService(pg.Execute(shell="/bin/sh", command="git clone https://github.com/mrblint/my-profile"))
node.addService(pg.Execute(shell="/bin/sh", command="my-profile/silly.sh"))
# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
