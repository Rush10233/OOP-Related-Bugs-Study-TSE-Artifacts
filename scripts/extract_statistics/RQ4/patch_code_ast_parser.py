from enum import Enum
from parse_ast import *
from concurrent.futures import ThreadPoolExecutor

class CodeStatus(Enum):
    invalid = 10
    context = 1
    deletion = 2
    addition = 3

def write_log(output_filename:str, statistics:list):
    outp_statistics=[statistic[0] + ':\t' + str(statistic[1]) for statistic in statistics]
    with open(output_filename, 'w') as f:
        f.write('\n'.join(outp_statistics))
        f.close()

def write_log_percentage(output_filename:str, statistics:list):
    total_nodes = sum([statistic[1] for statistic in statistics])
    data_percentage = ['{:.2f}%'.format((statistic[1] / total_nodes) * 100) for statistic in statistics]
    with open(output_filename, 'w') as f:
        for i in range(len(data_percentage)):
            f.write(statistics[i][0] + ':\t' + data_percentage[i] + '\n')
        f.close()



class PatchASTParser():
    def __init__(self, filedirname:str):
        self.statistic_context = {}
        self.statistic_buggy_code = {}
        self.statistic_patch = {}
        self.filedirname = filedirname
    
    def handle(self, nodes:list, status):
        nodes = [node.strip() for node in nodes if node.find('_') != -1]
        for node in nodes:
            if node.find('translation_unit') != -1:
                continue
            if status == CodeStatus.context:
                if node not in self.statistic_context:
                    self.statistic_context[node] = 1
                else:
                    self.statistic_context[node] = self.statistic_context[node] + 1
            if status == CodeStatus.deletion:
                if node not in self.statistic_buggy_code:
                    self.statistic_buggy_code[node] = 1
                else:
                    self.statistic_buggy_code[node] = self.statistic_buggy_code[node] + 1
            if status == CodeStatus.addition:
                if node not in self.statistic_patch:
                    self.statistic_patch[node] = 1
                else:
                    self.statistic_patch[node] = self.statistic_patch[node] + 1

    def calculate(self, filename, status):
        with open(filename, 'r') as f:
            code = f.read().split('\n\n')
            f.close()
        for snipt in code:
            snipt = snipt.encode()
            nodes = parse_tree(snipt)
            self.handle(nodes, status=status)

    def launch(self):
        filename_list_context=[]
        filename_list_buggy_code=[]
        filename_list_patch=[]
        for root, dirs, files in os.walk(self.filedirname):
            for file in files:
                if file.find('content') != -1:
                    filename_list_context.append(os.path.join(root, file))
                elif file.find('patch') != -1:
                    filename_list_patch.append(os.path.join(root, file))
                elif file.find('buggy') != -1:
                    filename_list_buggy_code.append(os.path.join(root, file))
        
        for filename in filename_list_buggy_code:
            self.calculate(filename, CodeStatus.deletion)
        for filename in filename_list_context:
            self.calculate(filename, CodeStatus.context)
        for filename in filename_list_patch:
            self.calculate(filename, CodeStatus.addition)
        
        output_buggy_code = sorted(self.statistic_buggy_code.items(),  key=lambda d: d[1], reverse=True)
        output_patch = sorted(self.statistic_patch.items(),  key=lambda d: d[1], reverse=True)
        output_context = sorted(self.statistic_context.items(),  key=lambda d: d[1], reverse=True)

        outp_file_name = self.filedirname[self.filedirname.rfind('/')+1 : ] + '.csv'
        write_log_percentage('../RQ4_node_percent_patch_' + outp_file_name, output_patch)
        write_log_percentage('../RQ4_node_percent_buggy_code_' + outp_file_name, output_buggy_code)
        write_log_percentage('../RQ4_node_percent_context_' + outp_file_name, output_context)
