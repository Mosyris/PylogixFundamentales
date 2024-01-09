from pylogix import PLC
# instance of PLC connection
with PLC() as comm:
    comm.IPAddress = '10.166.134.159'

    # Retrieves only a list of the program names
    programs = comm.GetProgramsList()
    print(programs.Value)
