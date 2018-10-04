from awscli.customizations.cloudformation.artifact_exporter import CloudFormationStackResource
from awscli.customizations.cloudformation.artifact_exporter import EXPORT_LIST

def awscli_initialize(cli):
    EXPORT_LIST.insert(0, CloudFormationStackResourceExtension)


class CloudFormationStackResourceExtension(CloudFormationStackResource):
    def do_export(self, resource_id, resource_dict, parent_dir):
        print 'CloudFormationStackResourceExtension.do_export'
        super(CloudFormationStackResourceExtension, self).do_export(resource_id, resource_dict, parent_dir)