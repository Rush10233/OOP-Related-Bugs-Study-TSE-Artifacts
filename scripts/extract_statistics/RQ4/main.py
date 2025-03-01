# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from analyzer import AnalyzerGCC
from analyzer import AnalyzerLLVM
from patch_code_ast_parser import PatchASTParser


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #analyzer1 = AnalyzerLLVM()
    #analyzer2 = AnalyzerGCC()
    #analyzer1.analyze_patch_files()
    #analyzer2.analyze_patch_files()
    parser = PatchASTParser('./gcc')
    parser.launch()
    parser = PatchASTParser('./llvm')
    parser.launch()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
