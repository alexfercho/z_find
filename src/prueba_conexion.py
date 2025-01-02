from netmiko import ConnectHandler

AT_x530L = {
    'device_type': 'cisco_ios',
    'host':   '172.22.32.19',
    'username': 'tqadmin',
    'password': 'L4cl4v3d31055w1tch35TQ1990*',
    'port' : 22,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}

net_connect = ConnectHandler(**AT_x530L)

#output = net_connect.send_command('show ip int brief')
output = net_connect.send_command('show int status')

print(output)
print(type(output))




if __name__ == "main":
    pass
