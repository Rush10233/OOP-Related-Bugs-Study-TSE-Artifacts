from tree_sitter import Language, Parser, Query
import os
import warnings

def write_tree_to_list(node, indent=0, outp:list=[]):
    current_line = ' ' * indent + f'{node.type}\n'
    outp.append(current_line)
    for child in node.children:
        # if child.type == 'namespace_definition':
        #     print('ok')
        write_tree_to_list(child, indent + 2, outp)



def parse_tree(source):
    warnings.simplefilter('ignore', FutureWarning)

    LANG_C = Language('build/my-languages.so', 'c')
    LANG_CPP = Language('build/my-languages.so', 'cpp')

    parser_c = Parser()
    parser_cpp = Parser()

    parser_c.set_language(LANG_C)
    parser_cpp.set_language(LANG_CPP)

    tree_cpp = parser_cpp.parse(source)
    res = []
    write_tree_to_list(node=tree_cpp.root_node, outp=res)
    return res
