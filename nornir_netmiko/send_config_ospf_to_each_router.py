from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")




def configure_ospf_csr1(task):
    """
    This function filters CSR1 and
    configures ospf on it.
    """
    filter_query = "172.16.60.200"
    # Filter inventory for the specific hostname which equal the filter value
    target_host = nr.filter(hostname=filter_query)
    for host in target_host.inventory.hosts.keys():
        if host == "CSR1":

            commands = ["int lo0",
                    "ip add 1.1.1.1 255.255.255.0",
                    "ip ospf network point-to-point",
                    "router ospf 1",
                    "network 172.16.60.0 0.0.0.255 area 0",
                ]

        


        
def configure_ospf_csr2(task):
    """
    This function filters CSR2 and
    configures ospf on it.
    """
    filter_query = "172.16.60.201"
    target_host = nr.filter(hostname=filter_query)
    for host in target_host.inventory.hosts.keys():
        if host == "CSR2":
         commands = ["int lo0",
                    "ip add 2.2.2.2 255.255.255.0",
                    "ip ospf network point-to-point",
                    "router ospf 1",
                    "network 172.16.60.0 0.0.0.255 area 0",
                ]
         


def configure_ospf_csr3(task):
    """
    This function filters CSR3 and
    configures ospf on it.
    """
    filter_query = "172.16.60.203"
    target_host = nr.filter(hostn=target_host)
    for host in target_host.inventory.hosts.keys():
        if host == "CSR3":
            commands = ["int lo0",
                        "ip add 3.3.3.3 255.255.255.0",
                        "ip ospf network point-to-point",
                        "router ospf 1",
                        "network 172.16.60.0 0.0.0.255 area 0",
                        ] 
            



    


