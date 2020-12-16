from tree_sitter import Language, Parser

# Store the library in the `build` directory
so_file_path = 'build/python-languages.so'
python_repo_path = '.'

# Build the *.so file
Language.build_library(so_file_path, python_repo_path)

PY_LANGUAGE = Language(so_file_path, 'python')

parser = Parser()
parser.set_language(PY_LANGUAGE)

source_bytes = bytes('''
def foo(required, optional=None):
    if bar:
        baz()
''', 'utf8')

tree = parser.parse(source_bytes)

root_node = tree.root_node

print()
print('type(tree) =', type(tree))
print('type(root_node) =', type(root_node))

print()
print('root_node.sexp() =', root_node.sexp())

def get_text(root):
    if root.type == 'identifier':
        return '--------' + source_bytes[root.start_byte:root.end_byte].decode('utf8')
    return ''

def dfs(root, indent=''):
    if root is None:
        return
    print(indent, root, get_text(root))
    for child in root.children:
        dfs(child, indent + '  ')

print()
dfs(root_node)
