from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_save_config
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")
filtered_hosts = nr.filter(F(groups__contains="cisco"))

def netmiko_send_config_file(task):
    try:
        task.run(task=netmiko_send_config, config_file="/home/hwtech/nornir_project/nornir_netmiko/config_file.txt")
    except FileNotFoundError:
        print("Unable to locate file please check the path of the file is correct")

def netmiko_save_my_config(task):
    task.run(task=netmiko_save_config)

results = filtered_hosts.run(task=netmiko_send_config_file)
print_result(results)

results = filtered_hosts.run(task=netmiko_save_my_config)
print_result(results)
