import os
import re
from utilities import *

class RTL:
    name = "none"
    final_contents = []
    cfg = []
    
    def __init__(self, path, file):
        self.name = file  
        # Remove unnecessary content from the file
        contents = read_file(os.path.join(path,file))
        for line in contents:
            self.final_contents.append(remove_whitespace(remove_comments(line)))

    def name(self):
        print(self.name)

    def get_CFG(self):
        return self.cfg

    def generate_CFG(self):
        always_condition = re.compile("always.*@\((.*)\)(.*)|always.*")
        if_condition = re.compile("if ?\((.*)\)(.*)")
        else_condition = re.compile("(^(?!.*if).*)(?<=else)(.*)")
        start_case_condition = re.compile("case ?\((.*)\)")
        case_condition = re.compile("(.*?):(.*)")
        begin_condition = re.compile("begin *$")
        end_condition = re.compile("end *$")
        end_case_condition = re.compile("endcase *$")
        assign_condition = re.compile("assign (.*)")
        
        parent_stack = []
        current_parent = None
        start_case_flag = False
        line_index = 0
        end = len(self.final_contents)

        while line_index < end:
            line = self.final_contents[line_index]
            # print("line: ", line)
            
            # Make the previous node as the parent for this begin block
            if begin_condition.search(line):
                if current_parent:
                    parent_stack.append(current_parent)
                current_parent = self.cfg[len(self.cfg)-1]
            
            elif end_condition.search(line):
                if parent_stack:
                    current_parent = parent_stack.pop()
                else:
                    current_parent = None

            elif always_condition.search(line):
                args = always_condition.search(line).group(1)
                if args:
                    for sym in args.split(','):
                        if '*' in sym:
                            node = Node('True == True', current_parent)
                        elif 'posedge' in sym:
                            node = Node(sym.split(' ')[1] + '== True', current_parent)
                        elif 'negedge' in sym:
                            node = Node(sym.split(' ')[1] + '== False', current_parent)
                else:
                    node = Node('True == True', current_parent)
                self.cfg.append(node)

            elif if_condition.search(line):
                regex = if_condition.search(line)
                condition = regex.group(1)
                node = Node(condition, current_parent)
                self.cfg.append(node)
                if regex.group(2).lstrip():
                    self.final_contents[line_index] = regex.group(2).lstrip()
                    line_index = line_index-1
            
            elif else_condition.search(line):
                condition = "<else block>"
                node = Node(condition, current_parent)
                self.cfg.append(node)
                if regex.group(2).lstrip():
                    self.final_contents[line_index] = regex.group(2).lstrip()
                    line_index = line_index-1

            elif start_case_condition.search(line):
                parameter = start_case_condition.search(line).group(1)
                start_case_flag = not start_case_flag
            
            elif case_condition.search(line) and start_case_flag:
                if (line.find(':') > line.find('[') and line.find('[') > 0):
                    node = Node(condition, current_parent)
                    self.cfg.append(node)
                    if parent_stack:
                        current_parent = parent_stack.pop()
                    else:
                        current_parent = None
                else:
                    regex = case_condition.search(line)
                    condition = parameter+'=='+regex.group(1)
                    node = Node(condition, current_parent)
                    self.cfg.append(node)
                    if regex.group(2).lstrip():
                        self.final_contents[line_index] = regex.group(2).lstrip()
                        line_index = line_index-1
            
            elif end_case_condition.search(line):
                start_case_flag = not start_case_flag

            elif assign_condition.search(line):
                condition = assign_condition.search(line).group(1)
                node = Node(condition, current_parent)
                self.cfg.append(node)
            
            else:
                if len(line.strip(' ')) and '=' in line and 'parameter' not in line:
                    node = Node(condition, current_parent)
                    self.cfg.append(node)
                    if parent_stack:
                        current_parent = parent_stack.pop()
                    else:
                        current_parent = None

            line_index = line_index + 1

class Node:
    number = -1
    parent = None
    condition = ""
    def __init__(self, c, p):
        self.number = -1
        self.parent = p
        self.condition = c
    def value(self):
        return self.condition
    def parent(self):
        return self.parent
    def print_node(self):
        print(self.number)
        print(self.parent)
        print(self.condition)
        print('\n')

