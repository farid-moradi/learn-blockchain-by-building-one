from hashlib import sha256

file = open("random_img.jpg", "rb")
hash = sha256(file.read()).hexdigest()
file.close()

print(f"The hash of my file is: {hash}")