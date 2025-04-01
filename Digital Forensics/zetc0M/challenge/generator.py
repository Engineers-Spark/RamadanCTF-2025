from scapy.all import *
import os
import random  


pcap_filename = "zetc0M.pcap"
image_filenames = ["image1.jpg", "image2.jpg", "aa.jpg", "image4.jpg"]  
src_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "10.10.1.4"]  
dst_ip = "192.168.1.100"  
src_port = 12345
dst_port = 80

# Check if all image files exist
for image_filename in image_filenames:
    if not os.path.exists(image_filename):
        print(f"Error: '{image_filename}' not found. Please ensure all files exist.")
        exit(1)


chunk_size = 1024
packets = []

for image_filename, src_ip in zip(image_filenames, src_ips):

    print(f"Processing '{image_filename}' with source IP {src_ip}...")
    with open(image_filename, "rb") as f:
        image_data = f.read()
    

    for i in range(0, len(image_data), chunk_size):
        chunk = image_data[i:i + chunk_size]
        packet = IP(src=src_ip, dst=dst_ip) / UDP(sport=src_port, dport=dst_port) / Raw(load=chunk)
        packets.append(packet)


print("Shuffling packets for time obfuscation...")
random.shuffle(packets)


wrpcap(pcap_filename, packets)
print("Done")
