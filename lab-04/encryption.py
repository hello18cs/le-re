# AES and RSA Encryption-Decryption in Python
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# ---------- AES IMPLEMENTATION ----------
def aes_encryption():
    data = b"Cloud Computing Security"
    key = get_random_bytes(16)  # 128-bit key
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    print("=== AES Encryption ===")
    print("Original Data:", data)
    print("Cipher Text:", ciphertext)
    # Decryption
    cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    decrypted_data = cipher_dec.decrypt(ciphertext)
    print("Decrypted Data:", decrypted_data, "\n")

# ---------- RSA IMPLEMENTATION ----------
def rsa_encryption():
    key_pair = RSA.generate(2048)
    public_key = key_pair.publickey()

    data = b"Virtual Machine Security"

    cipher_rsa = PKCS1_OAEP.new(public_key)
    ciphertext = cipher_rsa.encrypt(data)

    print("=== RSA Encryption ===")
    print("Original Data:", data)
    print("Cipher Text:", ciphertext)

    # Decryption
    cipher_rsa_dec = PKCS1_OAEP.new(key_pair)
    decrypted_data = cipher_rsa_dec.decrypt(ciphertext)
    print("Decrypted Data:", decrypted_data)
# ---------- MAIN ----------
if __name__ == "__main__":
    print("=== AES and RSA Encryption/Decryption Simulation ===\n")
    aes_encryption()
    rsa_encryption()
    # pip install pycryptodome
    # pip3 install pycrytodome