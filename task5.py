from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Determine protocol
        if protocol == 6:
            proto_name = "TCP"
        elif protocol == 17:
            proto_name = "UDP"
        else:
            proto_name = "Other"

        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}, Protocol: {proto_name}")

        # Print TCP/UDP payload data if applicable
        if proto_name == "TCP" and TCP in packet:
            print(f"TCP Payload: {packet[TCP].payload}")
        elif proto_name == "UDP" and UDP in packet:
            print(f"UDP Payload: {packet[UDP].payload}")

def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
