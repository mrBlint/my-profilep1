
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
node2 = request.XenVM("node2")
node3 = request.XenVM("node3")
node4 = request.XenVM("node4")
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node3.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node4.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node1.routable_control_ip = "true"
link = request.LAN("lan")
link.addInterface(iface1)
link.addInterface(iface2)
link.addInterface(iface3)
link.addInterface(iface4)
iface1 = node1.addInterface("if1")
iface1.component_id = "eth1"
iface1.addAddress(pg.IPv4Address("192.168.1.1","255.255.255.0"))
link.addInterface(iface2)
iface2 = node2.addInterface("if1")
iface2.component_id = "eth1"
iface2.addAddress(pg.IPv4Address("192.168.1.2","255.255.255.0"))
link.addInterface(iface3)
iface3 = node2.addInterface("if1")
iface3.component_id = "eth1"
iface3.addAddress(pg.IPv4Address("192.168.1.3","255.255.255.0"))
link.addInterface(iface4)
iface4 = node2.addInterface("if1")
iface4.component_id = "eth1"
iface4.addAddress(pg.IPv4Address("192.168.1.4","255.255.255.0"))

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="/bin/sh", command="sudo local/repository/silly.sh"))
# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
