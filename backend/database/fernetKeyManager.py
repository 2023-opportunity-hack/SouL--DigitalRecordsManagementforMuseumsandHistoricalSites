from cryptography.fernet import Fernet
import os

class FernetKeyManager:
    def __init__(self, key_file_path):
        self.key_file_path = key_file_path

    def get_key(self):
        if os.path.exists(self.key_file_path):
            with open(self.key_file_path, 'rb') as key_file:
                key = key_file.read()
                return key
        else:
            # key = Fernet.generate_key()
            # with open(self.key_file_path, 'wb') as key_file:
            #     key_file.write(key)
            # return key
            print("No Key Found!")
    def encrypt_password(self, password):
        f = Fernet(self.get_key())
        encrypted_password = f.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        f = Fernet(self.get_key())
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password
