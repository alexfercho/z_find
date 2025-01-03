#from netmiko import ConnectHandler
from netmiko import SSHDetect, ConnectHandler
#from netmiko.snmp_autodetect import SNMPDetect

AT_x530L = {
    'device_type': 'dell_os6',
    'host':   '172.22.32.45',
    'username': 'tqadmin',
    'password': 'L4cl4v3d31055w1tch35TQ1990*',
    'port' : 22,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}

net_connect = ConnectHandler(**AT_x530L)

#output = net_connect.send_command('show ip int brief')
output = net_connect.send_command('show interfaces status')
net_connect.enable()
print(output)
print(type(output))




"""device = {
    "device_type": "autodetect",
    "host": "172.22.32.45",
    "username": "tqadmin",
    "password": "L4cl4v3d31055w1tch35TQ1990*"
}
"""
"""
guesser = SSHDetect(**device)
best_match = guesser.autodetect()
print(best_match)  # Name of the best device_type to use further
print(guesser.potential_matches)  # Dictionary of the whole matching result
"""
# Update the 'device' dictionary with the device_type
#device["device_type"] = best_match

#with ConnectHandler(**device) as connection:
#    print(connection.find_prompt())


#if __name__ == "main":
#    pass