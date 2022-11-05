import scapy.all as scapy
import optparse

def user():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress",dest="ipAddress",help="Enter ip address")
    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ipAddress:
        print("Enter ip address")
    return user_input

def network(ip):
    arpRequest = scapy.ARP(pdst=ip)
    Broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = Broadcast/arpRequest
    answered = scapy.srp(packet,timeout=1,verbose=False)
    print("IP\t\t\tMAC Address\n---------------------------------------------")
    for element in answered:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)


userip = user()
network(userip.ipAddress)


