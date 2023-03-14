from crypto_app.des_algo import DES

def test_caesercipher():
    des = DES()
    
    key = "my_secret"
    message = "This is a secret message"
    crypt = "4c2b2e4c1fae6deae8c93d5106d13e6b"

    crypted = des.encrypt(message, key)
    assert crypted == "4c2b2e4c1fae6deae8c93d5106d13e6b"
    decrypted = des.decrypt(crypt, key)   
    assert decrypted == "Bonsoir"