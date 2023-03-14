from crypto_app.vigenerecipher_algo import VigenereCipher

def test_vigenere():
    """
    Un exemple de fonction de test, ici avec le cryptage
    blowfish.
    """

    vigenere = VigenereCipher()
    msg = "ceci est le test de vigenere"
    key = "clevigenere"

    encrypted = vigenere.encrypt(msg, key)
    decrypted = vigenere.decrypt(encrypted, key)
    assert decrypted == msg