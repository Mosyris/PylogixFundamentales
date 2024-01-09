from pycomm3 import LogixDriver
with LogixDriver ('10.166.134.147/12') as plc:
    print(plc)
    tags = plc._tags
# temp = plc.get_tag_list(progam='*')
for tag in tags:
    if 'stop' in tag or 'STOP' in tag or 'Stop' in tag:
        print(tag)