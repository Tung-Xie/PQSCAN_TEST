def get_tls_config():
    # [Low] TLS 1.3 混合模式與 PQC KEX
    tls_groups = [
        "X25519_MLKEM768",   # 混合模式
        "MLKEM768",          # 純 PQC
        "sntrup761",         # NTRU Prime (OpenSSH 常用)
        "hqc128",            # HQC
        "bikel1"             # BIKE
    ]

    # [Low] 傳統但高強度的 KEX
    traditional_kex = ["x448", "brainpoolp512r1"]

    # [Low] 隨機 PQC KEX 測試
    experimental = ["Frodo640aes", "kyber512", "Classic-McEliece-348864"]

    return {"groups": tls_groups + traditional_kex + experimental}

def encrypt_data():
    # [Medium] 雖然不是 PQC 但目前算安全
    algo = "aes-256-gcm"
    print(f"Encrypting with {algo}")