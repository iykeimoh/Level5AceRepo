import pyeapi
import yaml

pyeapi.load_config('eapi.conf')
file = open('vlans.yml', 'r')
file_vlan_dict = yaml.safe_load(file)

for switch in file_vlan_dict['switches']:
    connect = pyeapi.connect_to(switch)
    cmd_result = connect.enable ('show vlan')
    cmd_vlan_dict = cmd_result[0]['result']['vlans']
    print(f"for switch {switch}")
    for vlan in cmd_vlan_dict:
        vlan_id = vlan
        vlan_name = cmd_vlan_dict[vlan]['name']
        print(f"Vlan id of {vlan_id} with name {vlan_name}")

        print(cmd_vlan_dict [vlan] ['name'])


   




        
        




# print(cmd_result)