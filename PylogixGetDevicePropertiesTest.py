from pylogix import PLC
# instance of PLC connection
with PLC() as comm:
    comm.IPAddress = '10.166.134.143'

# Similar to GetModuleProperties, this queries a device at an IP address.
# This is useful for querying things that are not part of a chassis, like VFDs
   # single device properties

   # device = comm.GetDeviceProperties().Value
   # print(device.ProductName, device.Revision, device.IPAddress)

   # All devices properties

    device = comm.GetDeviceProperties()
    for d in device.Value:
        print(d.ProductName, d.Revision, d.IPAddress)

