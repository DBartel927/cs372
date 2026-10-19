# We want to write a function that will turn a dots-and-numbers IPv4 address into a packed byte string that contains those same numeric values.

# So for example, the address 1.2.3.255 should encode to a byte string of four bytes containing the values (in hex):

# 01 02 03 ff
# This would print out in Python as:

# b'\x01\x02\x03\xff'
# Here's some skeleton test code:

# def pack_ip(ip):
#     # IMPLEMENT ME

# test_data = (
#     ("0.0.0.0", b'\x00\x00\x00\x00'),
#     ("127.0.0.1", b'\x7f\x00\x00\x01'),
#     ("255.0.255.0", b'\xff\x00\xff\x00'),
#     ("127.1.127.1", b'\x7f\x01\x7f\x01'),
#     ("16.16.16.16", b'\x10\x10\x10\x10'),
#     ("1.1.1.1", b'\x01\x01\x01\x01'),
#     ("1.2.3.4", b'\x01\x02\x03\x04'),
# )

# for ip, packed_ip in test_data:
#     output = f"testing: {ip} -> {packed_ip}"
#     print(f"{output:<45}", end="")
#     print('OK' if pack_ip(ip) == packed_ip else 'FAIL')
# Hints:

# Don't forget to_bytes()! Or maybe the bytes() constructor.

# The int() function in Python will turn a string containing a number into a numeric value.

# The .split() string method is definitely useful.

def pack_ip(ip):
    # IMPLEMENT ME
    pieces = ip.split('.')
    return bytes(int(piece) for piece in pieces)

test_data = (
    ("0.0.0.0", b'\x00\x00\x00\x00'),
    ("127.0.0.1", b'\x7f\x00\x00\x01'),
    ("255.0.255.0", b'\xff\x00\xff\x00'),
    ("127.1.127.1", b'\x7f\x01\x7f\x01'),
    ("16.16.16.16", b'\x10\x10\x10\x10'),
    ("1.1.1.1", b'\x01\x01\x01\x01'),
    ("1.2.3.4", b'\x01\x02\x03\x04'),
)

for ip, packed_ip in test_data:
    output = f"testing: {ip} -> {packed_ip}"
    print(f"{output:<45}", end="")
    print('OK' if pack_ip(ip) == packed_ip else 'FAIL')