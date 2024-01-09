from pylogix import PLC
with PLC() as comm:
    comm.IPAddress = '10.166.134.159'
    time = comm.GetPLCTime()
    tags = comm.GetTagList()
    print("PLC Time:", time.Value)
    for t in tags.Value:
        print("Tag:", t.TagName, t.DataType)


