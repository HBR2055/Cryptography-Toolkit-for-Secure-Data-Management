import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    return kdf.derive(password.encode())

def encrypt_data(data, password):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return salt + iv + ciphertext

def decrypt_data(encrypted_data, password):
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded_data) + unpadder.finalize()

def encrypt_file(input_file, output_file, password):
    with open(input_file, "rb") as f:
        data = f.read()

    encrypted = encrypt_data(data, password)

    with open(output_file, "wb") as f:
        f.write(encrypted)

def decrypt_file(input_file, output_file, password):
    with open(input_file, "rb") as f:
        encrypted_data = f.read()

    decrypted = decrypt_data(encrypted_data, password)

    with open(output_file, "wb") as f:
        f.write(decrypted)