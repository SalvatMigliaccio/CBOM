import cryptography 
from cryptography.fernet import Fernet

#test function
key = Fernet.generate_key()
f = Fernet(key)
    
def encrypt_message(message):
    encoded_message = message.encode()
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_message):
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message

if __name__=="__main__":
    
    message="ciao"
    encrypted_message = encrypt_message(message)
    print(encrypted_message)
    
    decrypted_message=decrypt_message(encrypted_message)
    print(decrypted_message)