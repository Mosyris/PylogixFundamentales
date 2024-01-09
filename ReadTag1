from pylogix import PLC
with PLC() as comm:
    comm.IPAddress = '192.168.1.9'
    ret = comm.Read('MyTagName')
    print(ret.TagName, ret.Value, ret.Status)