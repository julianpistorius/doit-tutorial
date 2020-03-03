def task_imports():
    return {
        'actions': ['python -m import_deps '
                    'projects/requests/requests/models.py > requests.models.deps'],
    }
