from awscli.customizations.cloudformation.artifact_exporter import is_s3_url, is_local_file, make_abs_path
from awscli.customizations.cloudformation.yamlhelper import yaml_parse
from awscli.customizations.cloudformation.exceptions import InvalidTemplateUrlParameterError

def interpolate_local_includes(self, template_dict):
    if isinstance(template_dict, dict):
        for key, val in template_dict.items():
            if key == "Fn::Transform" and val.get("Name", None) == "AWS::Include":
                include = IncludeTransform(self.template_dir, val)
                if include.local():
                    del template_dict[key]
                    val = include.load()
                    template_dict.update(val)
            self.export_global_artifacts(val)
    elif isinstance(template_dict, list):
        for val in template_dict:
            self.export_global_artifacts(val)
    return template_dict

class IncludeTransform(object):

    PROPERTY_NAME = "Location"

    def __init__(self, dir, val):
        self.dir = dir
        self.parameters = val.get("Parameters", {});
        self.location = self.parameters.get(self.PROPERTY_NAME, {})

    def local(self):
        return not is_s3_url(self.location) and not self.location.startswith("https://s3.amazonaws.com/")

    def load(self):
        abs_path = make_abs_path(self.dir, self.location)
        if not is_local_file(abs_path):
            raise InvalidTemplateUrlParameterError(
                property_name=self.PROPERTY_NAME,
                resource_id="AWS::Include",
                template_path=abs_path)

        with open(abs_path, "r") as included_file:
            return yaml_parse(included_file.read())