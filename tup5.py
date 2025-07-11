from scapy.all import sniff, IP, TCP, UDP
import csv
import datetime

# Output CSV file
output_file = "five_tuple_log.csv"

# Open the file and write the header
with open(output_file, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["timestamp", "src_ip", "dst_ip", "src_port", "dst_port", "protocol"])

    def process_packet(pkt):
        # Check if it's an IP packet with TCP or UDP
        if IP in pkt and (TCP in pkt or UDP in pkt):
            ip_layer = pkt[IP]
            proto = "TCP" if TCP in pkt else "UDP"
            transport_layer = pkt[TCP] if TCP in pkt else pkt[UDP]
            
            row = [
                datetime.datetime.now().isoformat(),
                ip_layer.src,
                ip_layer.dst,
                transport_layer.sport,
                transport_layer.dport,
                proto
            ]
            writer.writerow(row)
            print(f"[+] {row}")

    print("📡 Capturing 5-tuple network traffic... Press Ctrl+C to stop.\n")
    
    try:
        sniff(filter="ip", prn=process_packet, store=0)
    except PermissionError:
        print("❌ You need to run this script with sudo.")
    except Exception as e:
        print(f"❌ Error: {e}")
