from scapy.all import IP
from scapy.all import ICMP
from scapy.all import sr1
while True:
  try:
    # we are trying to build packet
    src_ip = input("source ip> ")
    dst_ip = input("destination name> ")

    ip_head = IP(src=src_ip, dst=dst_ip)
    icmp_option = ICMP(id=1000)
    full_packet = ip_head / icmp_option

    packet_sender = sr1(full_packet)
    # to print reply
    if packet_sender:
       print(packet_sender.show())
    user_answer=input("to continue write  y ? ")
    if user_answer.lower()=="y":
       continue
    else:
     print ("good bye!")
     break
  except Exception:
    continue

