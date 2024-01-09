from pylogix import PLC
# instance of PLC connection
with PLC() as comm:
    comm.IPAddress = '10.166.134.159'

    # Requests properties of a specific module, Slot # needs to be specified
    device = comm.GetModuleProperties(5).Value
    print(device.ProductName, device.Revision)