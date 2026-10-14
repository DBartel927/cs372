# A packet in this protocol has the following format (lengths and offsets in bytes, integers are big-endian):

# Packet Layout
# Offset	Length	Description
# 0	2	The encoded message length
# 2	n	The message string encoded as UTF-8
# The encoded message length does not include the 2 bytes of the header. That is, a sample complete packet is:

# b'\x00\x02hi'
# So even though the total packet size is 4 bytes, the message is only 2 bytes.

# Determine if data contains a complete packet
# Write this function that accepts data, a byte string:

# def packet_complete(data):
# It returns true if there is at least one complete packet in the data, starting from offset 0.

# Extract the complete packet
# Write this function, which you can assume will only be called on complete packets:

# def packet_extract(data):
# This should return a tuple with two items:

# The complete packet including the message length
# Any remaining bytes after that packet
# The remaining bytes would be any part of the subsequent packet(s) that have been received.

# Skeleton Code
def packet_complete(data):
    if len(data) < 2:
        return False
    message_length = int.from_bytes(data[:2], byteorder='big')
    return len(data) >= 2 + message_length

def packet_extract(data):
    message_length = int.from_bytes(data[:2], byteorder='big')
    packet = data[:2 + message_length]
    remaining = data[2 + message_length:]
    return (packet, remaining)

test_data = (
    (b'\x00\x05hello', (True, (b'\x00\x05hello', b''))),
    (b'\x00\x05hello\x00\x03', (True, (b'\x00\x05hello', b'\x00\x03'))),
    (b'\x00\x05hello\x00\x03and\x00\x09bb', (True, (b'\x00\x05hello', b'\x00\x03and\x00\x09bb'))),
    (b'\x00\x00', (True, (b'\x00\x00',b''))),
    (b'\x00\x05hell', (False, None)),
    (b'\x00\x05', (False, None)),
    (b'\x00', (False, None)),
    (b'', (False, None)),
)

for data, (expected_complete, expected_result) in test_data:
    print(f"{'='*40}\nData: {data}\n{'-'*40}")

    complete = packet_complete(data)
    print(f"Expected: {expected_complete}")
    print(f"     Got: {complete}")
    assert(complete == expected_complete)

    if complete:
        result = packet_extract(data)
        print(f"Expected: {expected_result}")
        print(f"     Got: {result}")
        assert(result == expected_result)