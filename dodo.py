def task_imports():
    """find imports from a python module"""
    return {
        'file_dep': ['projects/requests/requests/models.py'],
        'targets': ['requests.models.deps'],
        'actions': ['python -m import_deps %(dependencies)s > %(targets)s'],
    }
