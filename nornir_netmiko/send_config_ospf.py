from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F
from random import randint

nr = InitNornir(config_file="config.yaml")
random_num = randint(1, 255)

def config_ospf_ny():
    commands = ["int lo0",
                f"ip add 1.1.1.1 255.255.255.0",
                "ip ospf network point-to-point",
                "router ospf 1",
                "network 172.16.60.0 0.0.0.255 area 0",
                ]
    filtered_hosts_ny = nr.filter(F(groups__contains="csr_ny"))
    results = filtered_hosts_ny.run(task=netmiko_send_config, config_commands=commands)
    return results
    

def config_ospf_la():
    commands = ["int lo0",
                f"ip add 2.2.2.2 255.255.255.0",
                "ip ospf network point-to-point",
                "router ospf 1",
                "network 172.16.60.0 0.0.0.255 area 0",
                ]
    filtered_hosts_la = nr.filter(F(groups__contains="csr_la"))
    results = filtered_hosts_la.run(task=netmiko_send_config, config_commands=commands)
    return results

def config_ospf_tor():
    commands = ["int lo0",
                f"ip add 3.3.3.3 255.255.255.0",
                "ip ospf network point-to-point",
                "router ospf 1",
                "network 172.16.60.0 0.0.0.255 area 0",
                ]
    filtered_hosts_tor = nr.filter(F(groups__contains="csr_tor"))
    results = filtered_hosts_tor.run(task=netmiko_send_config, config_commands=commands)
    return results



if __name__ == '__main__':
    config_ospf_ny()
    config_ospf_la()
    config_ospf_tor()


            



    


