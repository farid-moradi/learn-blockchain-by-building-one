# how Bob may verify Alice's message

from hashlib import sha256

secret_phrase = "secretkey"

def get_hash_with_secret_phrase(input_data, secret_phrase):
    combined = input_data + secret_phrase
    return sha256(combined.encode()).hexdigest()

print(get_hash_with_secret_phrase("this is an emale!", secret_phrase))

# then we should match the resulted hash with hash that we received from Alice to see if the
# integrity is met or not