from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = "Other"

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"

        print(f"\n[+] Packet Captured:")
        print(f"    From: {ip_layer.src}")
        print(f"    To  : {ip_layer.dst}")
        print(f"    Protocol: {protocol}")

        if Raw in packet:
            payload = packet[Raw].load
            try:
                print(f"    Payload: {payload[:100].decode('utf-8', errors='replace')}")
            except Exception as e:
                print("    Payload: [Unable to decode]")

def main():
    print("=== Packet Sniffer (Educational Use Only) ===")
    print("Capturing packets... Press Ctrl+C to stop.\n")

    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    main()
