from scapy.all import *


pcap_filename = "zetc0M.pcap"  
output_image = "flag.jpg"      
target_src_ip = "10.10.1.4"    


print(f"Reading packets from '{pcap_filename}'...")
try:
    packets = rdpcap(pcap_filename)
except FileNotFoundError:
    print(f"Error: '{pcap_filename}' not found.")
    exit(1)


filtered_packets = [p for p in packets if UDP in p and p[IP].src == target_src_ip]
if not filtered_packets:
    print(f"No UDP packets found for source IP {target_src_ip}. Check the PCAP or IP.")
    exit(1)


sorted_packets = sorted(filtered_packets, key=lambda p: p.time)


image_data = b''.join(p[Raw].load for p in sorted_packets)


with open(output_image, "wb") as f:
    f.write(image_data)

print("[*] Flag found") 
