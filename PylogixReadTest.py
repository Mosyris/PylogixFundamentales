from pylogix import PLC
# instance of PLC connection
with PLC() as comm:
    comm.IPAddress = '10.166.134.159'
# single tag read
    ret1 = comm.Read("diDE_SeqID")
    print(ret1.TagName, ret1.Value, ret1.Status)

# Read an array
    ret2 = comm.Read("SO01_CH16_FIO:0:C.Data", 5)
    print(ret2.TagName, ret2.Value, ret2.Status)

# Read a list of tags
    tags = ["daStd_GDU_Colors", "SO01_CH29", "SO01_CH30_Area"]
    ret3 = comm.Read(tags)

    # Print exactly how the data is returned
    print("returned data", ret3)

    # print each item returned
    for r in ret3:
        print(r.TagName, r.Value, r.Value)

