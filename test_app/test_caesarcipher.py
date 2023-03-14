from crypto_app.caesarcipher_algo import CaesarCipher

def test_caesercipher():
    caesercipher = CaesarCipher()
    key = 12
    message = "Bonsoir"
    crypt = "Nazeaud"
    crypted = caesercipher.encrypt(message, key)
    assert crypted == "Nazeaud"
    decrypted = caesercipher.decrypt(crypt, key)   
    assert decrypted == "Bonsoir"