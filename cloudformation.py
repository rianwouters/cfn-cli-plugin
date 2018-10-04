def initialize(cli):
    cli.register('building-command-table.cloudformation', inject_commands)

def inject_commands(command_table, session, **kwargs):
    print 'cloudformation.inject_commands'