from pylogix import PLC
# instance of PLC connection
with PLC() as comm:
    #comm.IPAddress = '10.166.134.159'
    #comm.IPAddress = '11.200.0.120'
    comm.IPAddress = '11.200.0.7'


# Sends a broadcast request out on the network, and return basic info of all the connected devices
    devices = comm.Discover()
    for device in devices.Value:
        print(device.ProductName, device.Revision, device.IPAddress,)