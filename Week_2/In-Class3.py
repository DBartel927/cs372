# There might be Python built-ins to do this, but we want to do it by hand to figure out how it works.

# Write a function that given an array of 4 bytes representing an IP address and another array of 4 bytes representing a subnet mask, return a two-part tuple that contains an array representing the network portion and an array representing the host portion.

# In the examples below, the inputs are shown as IP/subnet tuples, and the outputs are shown as network/host tuples

# Input                              Output:
# ─────────────────────────────────  ────────────────────────────
# ([192,168,17,2], [255,0,0,0])      ([192,0,0,0], [0,168,17,2])
# ([192,168,17,2], [255,255,0,0])    ([192,168,0,0], [0,0,17,2])
# ([192,168,17,2], [255,255,255,0])  ([192,168,17,0], [0,0,0,2])
# ([192,168,17,2], [255,192,0,0])    ([192,128,0,0], [0,40,17,2])
# ([192,168,17,2], [255,255,248,0])  ([192,168,16,0], [0,0,1,2])
# Hints:

# Bitwise AND of two numbers in Python: a & b.

# Bitwise unsigned invert of a single byte in Python is a little weird, but looks like this:

# ~a & 0xff
# If you don't AND with 0xff, it will give you a negative two's-complement answer.

def split_ip(ip, subnet):
    network = []
    host = []
    for i in range(4):
        net_byte = ip[i] & subnet[i]
        network.append(net_byte)
        host_byte = ip[i] & (~subnet[i] & 0xff)
        host.append(host_byte)
    return (network, host)

print(split_ip([192, 168, 17, 2], [255, 0, 0, 0]))
print(split_ip([192, 168, 17, 2], [255, 255, 0, 0]))
print(split_ip([192, 168, 17, 2], [255, 255, 255, 0]))
print(split_ip([192, 168, 17, 2], [255, 192, 0, 0]))
print(split_ip([192, 168, 17, 2], [255, 255, 248, 0]))