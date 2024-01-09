from pylogix import PLC
# instance of PLC connection
with PLC() as comm:
    comm.IPAddress = '10.166.134.159'

    # retrieve the list of tags of a particular program
    program_tags = comm.GetProgramTagList("Program:Conveyor")
    for t in program_tags.Value:
        print("Tag:", t.TagName, t.DataType)