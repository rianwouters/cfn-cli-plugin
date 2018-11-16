# Solutions for selected ```cloudformation package``` issues

## Introduction
This AWS CLI plugin implements the following CloudFormation package command features:

1. Add the node_modules directory or use a custom path as its search path
2. Recursively interpolate local files included by the include transform

## Add the node_modules directory or use a custom path as its search path
If you use the AWS CLI to package your cloudformation templates, it will only allow you to use local subdirectories.
However, in certain cases you may want to have cloudformation look into other directories as well.   
This plugin extends the ```aws cloudformation``` command to search in multiple directories.

By default, cloudformation searches only the template directory.
This plugin defaults to searching the template directory and the node_modules directory.
The environment variable CFN_PACKAGE_PATHS can be used to specify any path list.  

### Typical use case
You have a cloudformation stack A that includes some lambda function code and you want to reuse different versions of this stack in multiple application stacks.
For example, you may want to deploy a bug fix for one application, but not for another.
Having it's own lifecycle, you archive A's template and lambda sources in a separate git archive.

You can use ```npm install``` to install A as a module in an application.
You can then refer to the template of A by using code URI ```'node_modules/A/template.yml'```
Your application is now using an npm-controlled version of stack A, which is fine.

However, a problem arises when you try to include stacks recursively (on top of the ugliness of refering to ```node_modules``` in the template).
If an npm module refers to node_modules, cfn package will search for it relative to the template location.
That's where this plugin comes in handy!

Installing this plugin will allow you to
- recursively reuse versioned CloudFormation components
- refer to any CloudFormation component without referencing the node_modules directory

## Recursively interpolate local files included by the include transform

By default files included by the include transform are uploaded. However

1. Files referenced by the included files are not uploaded
2. Shortform intrinsic functions are not expanded

Both issues are solved by interpolating the included local files instead of uploading them.
This way, the package command will also upload the files recursively referenced by the included files, and expand any shortform intrinsic function.  

## Prerequisites
- python
- pip

## Installation
```pip install -U git+https://github.com/rianwouters/cfn-cli-plugin```
