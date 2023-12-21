from scapy.all import ARP, Ether, srp

def arp_scan(ip):
    arp_request = ARP(pdst=ip)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address
    packet = ether_frame / arp_request

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    target_ip = "10.0.2.0/24"  # Replace with your target IP range
    scan_result = arp_scan(target_ip)

    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in scan_result:
        print(f"{device['ip']}\t\t{device['mac']}")
