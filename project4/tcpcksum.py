def pack_ip(ip):
    pieces = ip.split('.')
    return bytes(int(piece) for piece in pieces)

def make_pseudo_header(source_ip, dest_ip, tcp_length):
    pseudo_header = pack_ip(source_ip)
    pseudo_header += pack_ip(dest_ip)
    pseudo_header += b"\x00"
    pseudo_header += b"\x06"
    pseudo_header += tcp_length.to_bytes(2, "big")
    return pseudo_header

def checksum(data):
    if len(data) % 2 == 1:
        data += b"\x00"
    total = 0
    offset = 0
    while offset < len(data):
        word = int.from_bytes(data[offset:offset + 2], "big")
        total += word
        total = (total & 0xffff) + (total >> 16)
        offset += 2
    return (~total) & 0xffff

def validate_packet(index):
    with open(f"tcp_addrs_{index}.txt", "r") as fp:
        addresses = fp.read().split()
    source_ip = addresses[0]
    dest_ip = addresses[1]
    with open(f"tcp_data_{index}.dat", "rb") as fp:
        tcp_data = fp.read()
    tcp_length = len(tcp_data)
    pseudo_header = make_pseudo_header(source_ip, dest_ip, tcp_length)
    original_checksum = int.from_bytes(tcp_data[16:18], "big")
    tcp_zero_checksum = (tcp_data[:16] + b"\x00\x00" + tcp_data[18:])
    calculated_checksum = checksum(pseudo_header + tcp_zero_checksum)
    return original_checksum == calculated_checksum

for i in range(10):
    if validate_packet(i):
        print("PASS")
    else:
        print("FAIL")