from nornir import InitNornir
from nornir_utils.plugins.functions import print_title

nr = InitNornir(config_file="config.yaml")

# To print hosts in inventory
filter_query = "172.16.60.200"
target_host = nr.filter(hostname=filter_query)
for host in target_host.inventory.hosts.keys():
    print(host)
        

        

