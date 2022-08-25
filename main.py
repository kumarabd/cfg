from utilities import *
from cfg import *
from graph import *

base_path = '/Users/abishekk/Documents/github-projects/utd/RTL-File-generation/RTL/All_RTL'
rtl_files_path = os.path.join(base_path, 'RTLFiles.txt')

rtl_file_list = read_file(rtl_files_path)

for file in rtl_file_list:
    #file = "adbg_axi_biu.sv"
    print("File: ",file)
    print("--------------------------------------------------------------------")
    print("********************************************************************")
    print("--------------------------------------------------------------------")
    obj = RTL(base_path, remove_whitespace(file))
    obj.generate_CFG()

    # Build the graph
    gr = Graph(obj.get_CFG())
    gr.show()
