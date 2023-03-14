from crypto_app.aes_algo import AdvancedEncryptionStandard

def test_aes():
    """
    Un exemple de fonction de test, ici avec le cryptage
    AES.
    """

    aes = AdvancedEncryptionStandard()
    msg = "cleaes"
    key = "abcdefghijklmnopqrstuvwx"

    encrypted = aes.encrypt(msg, key)
    assert encrypted == "32f306250f5c"
    decrypted = aes.decrypt(encrypted, key)
    assert decrypted == msg