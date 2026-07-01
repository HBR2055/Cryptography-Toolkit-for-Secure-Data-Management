import json
import os
from crypto_utils import encrypt_data, decrypt_data

VAULT_FILE = "vault.dat"

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.data = {}
        self.load_vault()

    def load_vault(self):
        if not os.path.exists(VAULT_FILE):
            self.data = {}
            return

        with open(VAULT_FILE, "rb") as f:
            encrypted = f.read()

        try:
            decrypted = decrypt_data(encrypted, self.master_password)
            self.data = json.loads(decrypted.decode())
        except:
            print("Incorrect master password!")
            self.data = {}

    def save_vault(self):
        encrypted = encrypt_data(json.dumps(self.data).encode(), self.master_password)
        with open(VAULT_FILE, "wb") as f:
            f.write(encrypted)

    def add_entry(self, service, username, password):
        self.data[service] = {"username": username, "password": password}
        self.save_vault()

    def get_entry(self, service):
        return self.data.get(service, "Not found")

    def list_services(self):
        return list(self.data.keys())