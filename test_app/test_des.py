from crypto_app.des_algo import DES

def test_des():
    des = DES()
    
    key = "mysecret"
    message = "This is a secret message"
    crypt = "fcedd1515146aab639575b874c72dc006b2142c540562601f5f26349eefb43d9"

    crypted = des.encrypt(message, key)
    assert crypted == "fcedd1515146aab639575b874c72dc006b2142c540562601f5f26349eefb43d9"
    decrypted = des.decrypt(crypt, key)   
    assert decrypted == "This is a secret message"