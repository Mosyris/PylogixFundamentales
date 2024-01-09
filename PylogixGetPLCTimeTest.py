from pylogix import PLC
# instance of PLC connection
with PLC() as comm:
    comm.IPAddress = '10.166.134.159'

    # read the plc clock and return the time
    time = comm.GetPLCTime()
    print("PLC Time:", time.Value)

    raw_time = comm.GetPLCTime(True)
    print("Raw Time:", raw_time.Value)