import ipaddress
from os import system

def hostips(network):
    """This function will print out the total number of ussable IPs"""
    numhostips = []
    v4Net = ipaddress.ip_network(network)
    numhosts = v4Net.hosts()

    for x in numhosts:
        numhostips.append(str(x))
    return numhostips

def firsthostip(network):
    """This function will print out the first usable IP for this subnet"""
    numhostips = []
    v4Net = ipaddress.ip_network(network)
    numhosts = v4Net.hosts()

    for x in numhosts:
        numhostips.append(str(x))

    return numhostips[0]

def lasthostip(network):
    """This function will return the last usable IP for this subnet"""
    numhostips = []
    v4Net = ipaddress.ip_network(network)
    numhosts = v4Net.hosts()

    for x in numhosts:
        numhostips.append(str(x))

    return numhostips[-1]

def netmask(network):
    dottedDecimalNetmask = ipaddress.ip_network(network)
    return dottedDecimalNetmask.netmask.compressed

def wildcard_mask(network):
    """This function will print out the wildcard mask for the subnet range"""
    wildcardMask = ipaddress.ip_network(network)

    return wildcardMask.hostmask.compressed

def main():
    """
    :return: This is the main() function that invokes/call the other functions
    when this module is run as a script. If not being run as a script, the main()
    function will never be called
    """
    system('')
    network = input('Please enter a network/network i.e., 10.0.0.0/27:')
    print()

    totalIP = hostips(network)
    print('The total number of usable IPs in the network is', len(totalIP), 'usable IPs')

    firstIP = firsthostip(network)
    print('The FIRST usable IP address is:', firstIP)

    lastIP = lasthostip(network)
    print('The LAST usable IP address within that network is', lastIP)

    wcMask = wildcard_mask(network)
    print('The wildcard mask for the subnet would be:', wcMask)
    
    dottedMask = netmask(network)
    print('The dotted-deciaml notation for the subnet mask would be:', dottedMask)

if __name__ == '__main__':
    main()
