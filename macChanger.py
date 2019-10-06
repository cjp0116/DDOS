#!/usr/bin/env/python
import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC add>
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify an new mac, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfigResult = subprocess.check_output(["ifconfig", options.interface])
    macAddressSearchResults = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfigResult)

    if macAddressSearchResults:
        return macAddressSearchResults.group(0)
    else:
        print("[-] Could not read MAC address.")

options = get_arguments()
currentMac = get_current_mac(options.interface)
print("Current MAC: " + currentMac)

change_mac(options.interface, options.new_mac)
#!/usr/bin/env/python
import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC add>
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify an new mac, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfigResult = subprocess.check_output(["ifconfig", options.interface])
    macAddressSearchResults = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfigResult)

    if macAddressSearchResults:
        return macAddressSearchResults.group(0)
    else:
        print("[-] Could not read MAC address.")

options = get_arguments()
currentMac = get_current_mac(options.interface)
print("Current MAC: " + currentMac)

if currentMac == options.new_mac:
    print("[+] MAC address was successfully changed to :" + currentMac)
else:
    print("[-] MAC address did not get changed")


 


