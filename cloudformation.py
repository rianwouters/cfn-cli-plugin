from awscli.customizations.cloudformation import artifact_exporter
from package.search_path import search_abs_path
from package.local_includes import interpolate_local_includes

def awscli_initialize(cli):
    artifact_exporter.make_abs_path = search_abs_path
    artifact_exporter.Template.export_global_artifacts = interpolate_local_includes
