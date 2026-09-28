# Get a Unicode string that has some special character in it. Here's one you can copy:

# "Hi 🙂"
# Encode it into bytes with encoding "utf-8".

# Print the bytes. (See the helper function, below.)

# Encode it into bytes with encoding "ascii". What happens?

# Encode it into bytes with encoding "utf-16".

# Print the bytes. How do they differ from the UTF-8 encoding?

# Take the bytes you encoded into UTF-16. Try to decode them as "utf-8". What happens?

# Decode the bytes as "utf-16" and print the result. Verify it matches the original string.

s = "Hi 🙂"

a = s.encode("utf-8")

print(a)

# b'Hi \xf0\x9f\x99\x82'

# b = s.encode("ascii")

# print(b)

# What happens: UnicodeEncodeError: 'ascii' codec can't encode character '\U0001f642' in position 3: ordinal notin range(128)

c = s.encode("utf-16")

print(c)

# Output: b'\xff\xfeH\x00i\x00 \x00=\xd8B\xde'

d = c.decode("utf-8")

# If try to decode with "utf-8": UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

print(d)

# Output: Hi 🙂