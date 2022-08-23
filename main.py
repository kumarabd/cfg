from utilities import *
from cfg import *

base_path = '/Users/kabishek/Documents/RTL-File-generation/RTL/All_RTL'
rtl_files_path = os.path.join(base_path, 'RTLFiles.txt')

rtl_file_list = read_file(rtl_files_path)

rtl_group = []

for file in rtl_file_list:
    file = "adbg_axi_biu.sv"
    print("File: ",file)
    print("--------------------------------------------------------------------")
    print("********************************************************************")
    print("--------------------------------------------------------------------")
    obj = RTL(base_path, remove_whitespace(file))
    obj.generate_CFG()
    rtl_group.append(obj)
    # print(obj.get_CFG())

    for ob in obj.get_CFG():
        ob.print_node()

# print(rtl_group)