from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
# The F object allows us to do advanced filtering of hosts
from nornir.core.filter import F

def sending_netmiko_command(task):
    commands = ["show ip int br | ex una", "show run all | se ospf"]
    for command in commands:
        task.run(task=netmiko_send_command, command_string=command)

# Specify the name of the group we want to run the task on
target_group = "cisco"

def main():
    nr = InitNornir(config_file="config.yaml")
    # The F object let's you access the magic methods of each types by 
    # just prepeding two underscores and the the name of the magic method. 
    filtered_hosts = nr.filter(F(groups__contains="cisco"))
    results = filtered_hosts.run(task=sending_netmiko_command)
    print_result(results)

main()