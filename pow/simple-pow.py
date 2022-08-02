from hashlib import sha256

x = 5
y = 0

while sha256(f'{x * y}'.encode()).hexdigest()[-5:] != "00000":
    print(sha256(f'{x * y}'.encode()).hexdigest())
    y += 1

print(sha256(f'{x * y}'.encode()).hexdigest())
print(f'The solution is y = {y}')