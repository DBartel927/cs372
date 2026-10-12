# Write this function:

# def encode_data(message, value):
# message is a string
# value is a signed integer value
# The return value should be a byte array that contains the following information (offsets and lengths are in bytes):

# Offset │ Length │ Description
# ───────┼────────┼──────────────────────────────────────────────────
#   0    │    2   │ Total encoded length, including message and value
#   2    │    n   │ The message string encoded as UTF-8
#  2+n   │    4   │ The value encoded as 4-byte 2's complement
# Then write this function, the inverse of the first one:

# def decode_data(data):
# This should take the data from your encode_data() function and return a tuple containing the message (decoded to a string) and the value (decoded to an integer).

# If everything works well, the decoded values will match the encoded ones.

def encode_data(message, value):
    message_bytes = message.encode("utf-8")
    value_bytes = value.to_bytes(4, byteorder="big", signed =True)
    length = 2 + len(message_bytes) + 4
    length_bytes = length.to_bytes(2, byteorder="big")
    return bytearray(length_bytes + message_bytes + value_bytes)

def decode_data(data):
    message = data[2:-4].decode("utf-8")
    value = int.from_bytes(data[-4:], byteorder="big", signed=True)
    return (message, value)

message = "It's me a computer!"
value = -88

encoded = encode_data(message, value)
print(encoded)
decoded = decode_data(encoded)
print(decoded)