from scapy.all import sniff

# Function to handle packets
def process_packet(packet):
    if packet.haslayer('IP'):
        ip_layer = packet['IP']
        print(f"Source IP: {ip_layer.src} -> Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
        if packet.haslayer('Raw'):
            print(f"Payload: {packet['Raw'].load}")
        print("-" * 50)

# Start sniffing packets
print("Starting packet sniffer... (Press CTRL+C to stop)")
sniff(prn=process_packet, count=10)  # Captures 10 packets and stops
