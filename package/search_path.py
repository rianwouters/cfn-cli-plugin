from awscli.customizations.cloudformation.artifact_exporter import make_abs_path
from os.path import join, exists, isabs
from os import environ

def search_paths():
    if 'CFN_PACKAGE_PATH' in environ:
        p = environ.get("CFN_PACKAGE_PATHS").split(';')
    else:
        p = ['node_modules']
    p.append('');
    return p

def search_abs_path(base_path, path):
    for search_path in search_paths():
        if not isabs(search_path):
            search_path = join(base_path, search_path)
        abs_path = make_abs_path(search_path, path)
        if exists(abs_path):
            return abs_path
    return abs_path
