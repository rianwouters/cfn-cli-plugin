from awscli.customizations.cloudformation import artifact_exporter
from os.path import join, exists

org_make_abs_path = artifact_exporter.make_abs_path

def make_abs_path(base_path, path):
    for search_path in ['node_modules', '']:
        abs_path = org_make_abs_path(join(base_path, search_path), path)
        if exists(abs_path):
            return abs_path
    return abs_path

def awscli_initialize(cli):
    artifact_exporter.make_abs_path = make_abs_path