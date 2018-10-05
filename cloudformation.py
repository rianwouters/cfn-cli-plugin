import awscli.customizations.cloudformation.artifact_exporter
import os

org_make_abs_path = artifact_exporter.make_abs_path

def make_abs_path(directory, path):
    for search_path in [' ' , 'node_modules']:
        abs_path = org_make_abs_path(os.path.join(directory, search_path), path)
        print 'Searching ' + search_path
        if os.path.isdir(abs_path) or os.path.isfile(abs_path):
            return abs_path
    return abs_path

def awscli_initialize(cli):
    artifact_exporter.make_abs_path = make_abs_path