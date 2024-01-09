from pycomm3 import LogixDriver
with LogixDriver ('10.166.134.159/0') as plc:
    print(plc.info)
 #   tags = plc._tags
# temp = plc.get_tag_list(progam='*')
#for tag in tags:
 #       print(tag)