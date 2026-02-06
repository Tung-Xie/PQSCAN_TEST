import hashlib

def hash_comparison():
    # [Low] PQC 友好的 Hash
    h1 = hashlib.sha3_512()
    h2 = hashlib.sha3_256()
    h3 = hashlib.shake_256()

    # [Medium] 目前主流安全
    h4 = hashlib.sha512()
    h5 = hashlib.sha256()

    # [Critical/High] 用來對比的舊算法
    bad_h1 = "md5"
    bad_h2 = "sha1"

    print("Hashing assets initialized.")

def pqc_encryption_strings():
    # 塞入清單中的 Encryption 相關字串供掃描
    pqc_enc = ["ML-KEM-1024", "kyber1024", "Frodo1344shake"]
    return pqc_enc