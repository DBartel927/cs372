# IP Address to Decimal Value
# Here are three IPv4 addresses. Convert them to 4-byte decimal values.

# 192.168.1.2
# 10.20.30.40
# 127.0.0.1
# Hint: Bitwise shift and OR.

# Decimal Value to IP Address
# Here are three decimal values. They are all 4 bytes, each representing an IP address:

# 3325256824
# 3405803976
# 3221225987
# Give the corresponding IP addresses in dots-and-numbers format.

# Hint: Bitwise shift and AND.

# What to Submit
# Your completed code
# The answers to the conversions in a code comment

def ip_to_decimal(ip):
    a, b, c, d = map(int, ip.split('.'))
    return (a << 24) + (b << 16) + (c << 8) + d

ip1 = ip_to_decimal("192.168.1.2")
ip2 = ip_to_decimal("10.20.30.40")
ip3 = ip_to_decimal("127.0.0.1")

# Decimal Value to IP Address
def decimal_to_ip(decimal):
    return f"{(decimal >> 24) & 0xFF}.{(decimal >> 16) & 0xFF}.{(decimal >> 8) & 0xFF}.{decimal & 0xFF}"

ip4 = decimal_to_ip(3325256824)
ip5 = decimal_to_ip(3405803976)
ip6 = decimal_to_ip(3221225987)

# Answers:
# 192.168.1.2 -> 3232235778
# 10.20.30.40 -> 169090600
# 127.0.0.1 -> 2130706433
# ip1, ip2, ip3 contain the decimal values for the IP addresses
# ip4, ip5, ip6 contain the IP addresses for the decimal values
# 3325256824 -> 198.51.100.8
# 3405803976 -> 203.0.113.8
# 3221225987 -> 192.0.2.3

print(ip1, ip2, ip3)
print(ip4, ip5, ip6)