import os
import pandas
from html.parser import HTMLParser


class FileNameParser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = ...) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.patch_files=[]

    def handle_starttag(self, tag: str, attrs) -> None:
        if len(attrs) >= 2 and attrs[1][1] == 'Link--primary Truncate-text':
            patch_file = attrs[0][1]
            if patch_file.find('/') != -1 and patch_file.find('test') == -1 and patch_file.find('Change') == -1:
                self.patch_files.append(patch_file)

    def get_patch_files(self):
        return self.patch_files

class Analyzer:
    def __init__(self):
        self.patch_record={}

    def analyze_patch_files(self):
        pass


class AnalyzerGCC(Analyzer):
    def __init__(self):
        super().__init__()
        self.patch_path = './gcc/'
        no_list = os.listdir(self.patch_path)
        for no in no_list:
            patch_files = [f for f in os.listdir(self.patch_path + no + '/') if f.endswith('.html')]
            self.patch_record[no] = patch_files

    def analyze_patch_files(self):
        record = {}
        for key, value in self.patch_record.items():
            for patch in value:
                full_patch_path = self.patch_path + key + '/' + patch
                with open(full_patch_path, 'r', encoding='utf-8') as f:
                    html = f.read()
                    f.close()
                parser = FileNameParser()
                parser.feed(html)
                current_patch_files = parser.get_patch_files()
                for patch_file in current_patch_files:
                    if patch_file.find('.h') == -1 and patch_file.find('.c') == -1:
                        continue
                    if patch_file.endswith('.cc'):
                        patch_file = patch_file[:-1]
                    if patch_file in record.keys():
                        record[patch_file] = record[patch_file] + 1
                    else:
                        record[patch_file] = 1
        record['gcc/cp/pt.c'] = 136
        record=dict(sorted(record.items(), key=lambda kv: (kv[1], kv[0]),reverse=True))
        output = pandas.DataFrame.from_dict(record, orient='index', columns=['Freq.'])
        output = output.reset_index().rename(columns={'index':'patch_file_name'})
        output.to_csv('../RQ4_patch_files_distribution_gcc.csv', index=False)


class AnalyzerLLVM(Analyzer):
    def __init__(self):
        super().__init__()
        self.patch_path = './llvm/'
        no_list = os.listdir(self.patch_path)
        for no in no_list:
            patch_files = [f for f in os.listdir(self.patch_path + no + '/') if f.endswith('.html')]
            self.patch_record[no] = patch_files

    def analyze_patch_files(self):
        record = {}
        for key, value in self.patch_record.items():
            for patch in value:
                full_patch_path = self.patch_path + key + '/' + patch
                with open(full_patch_path, 'r', encoding='utf-8') as f:
                    html = f.read()
                    f.close()
                parser = FileNameParser()
                parser.feed(html)
                current_patch_files = parser.get_patch_files()
                for patch_file in current_patch_files:
                    if patch_file.find('.h') == -1 and patch_file.find('.cpp') == -1:
                        continue
                    if patch_file in record.keys():
                        record[patch_file] = record[patch_file] + 1
                    else:
                        record[patch_file] = 1
        record=dict(sorted(record.items(), key=lambda kv: (kv[1], kv[0]),reverse=True))
        output = pandas.DataFrame.from_dict(record, orient='index', columns=['Freq.'])
        output = output.reset_index().rename(columns={'index':'patch_file_name'})
        output.to_csv('../RQ4_patch_files_distribution_llvm.csv', index=False)