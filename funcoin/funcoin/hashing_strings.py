import hashlib

# hash functions expect bytes as input: the encode() method turns strings to bytes
input_bytes = b"backpack"

output = hashlib.sha256(input_bytes)

# we use hexdigest() to convert bytes to hex because it's easier to read
print(output.hexdigest())