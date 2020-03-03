import pathlib
import pygraphviz


def module_to_dot(dependencies, targets):
    graph = pygraphviz.AGraph(strict=False, directed=True)
    for dep in dependencies:
        filepath = pathlib.Path(dep)
        source = filepath.stem
        with filepath.open() as fh:
            for line in fh:
                sink = line.strip()
                if sink:
                    graph.add_edge(source, sink)
    graph.write(targets[0])


def task_imports():
    """find imports from a python module"""
    return {
        'file_dep': ['projects/requests/requests/models.py'],
        'targets': ['requests.models.deps'],
        'actions': ['python -m import_deps %(dependencies)s > %(targets)s'],
    }


def task_dot():
    """generate a graphviz's dot graph from module imports"""
    return {
        'file_dep': ['requests.models.deps'],
        'targets': ['requests.models.dot'],
        'actions': [module_to_dot],
    }
