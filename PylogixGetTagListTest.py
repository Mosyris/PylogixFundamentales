from pylogix import PLC
# instance of PLC connection
with PLC() as comm:
    comm.IPAddress = '10.166.134.159'

# retrieve all the tags custom formated
    tags = comm.GetTagList()
    for t in tags.Value:
        print("Tag:", t.TagName, t.DataType)