import requests
import netmiko
import json
from netmiko import ConnectHandler


credenciales = ("cisco", "cisco123!")

conect = netmiko.ConnectHandler(
    device_type= 'cisco_ios',
    host= '192.168.56.102',
    username= 'cisco',
    password='cisco123!'
)
output = conect.send_command('show ip interface brief\n')
input("Presiona Enter para ver el resultado de (show ip interface brief)...")
print(output)

output1 = conect.send_command('show running-config\n')
input("Presiona Enter para ver el resultado de (show running-config)...")
print(output1)

output2 = conect.send_command('show version\n')
input("Presiona Enter para ver el resultado de (show version)...")
print(output2)



