from crypto_app.blowfish_algo import Blowfish

def test_blowfish():
    caesercipher = Blowfish()
    key = "ceciestuneclef"
    message = "Bonsoir"
    crypted = caesercipher.encrypt(message, key)
    decrypted = caesercipher.decrypt(crypted, key)   
    assert decrypted == "Bonsoir"