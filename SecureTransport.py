def get_cipher_suites():
    # --- AEAD (認證加密) ---
    # [Medium] 傳統高效能 AEAD
    aead_standard = [
        "AES-256-GCM", 
        "AES-128-GCM", 
        "CHACHA20-POLY1305"
    ]

    # --- PQC KEM 混合模式 (KEX) ---
    # [Low] 混合與純 PQC
    pqc_kex = [
        "X25519_MLKEM768", 
        "p256_kyber512",
        "sntrup761x25519-sha512@openssh.com"
    ]

    return {"AEAD": aead_standard, "PQC_KEX": pqc_kex}