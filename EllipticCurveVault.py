def get_ecc_inventory():
    # [Medium] 2025 主流安全曲線 (傳統加密但強度足夠)
    secure_curves = [
        "secp256r1", "secp384r1", "secp521r1", 
        "brainpoolp256r1", "x25519", "x448", "ed25519"
    ]

    # [High/Critical] 風險曲線 (強度不足或已棄用)
    risky_curves = [
        "secp160k1", "secp192r1", "sect163r2", 
        "sect233k1", "sect283r1", "sect571k1"
    ]

    # [Low] PQC 混合型曲線
    pqc_hybrid = ["p256_frodo640aes", "x25519_kyber768_draft00"]

    return {"safe": secure_curves, "risky": risky_curves, "pqc": pqc_hybrid}

def ecc_function_call():
    # 模擬 Crypto Function Call
    curves = get_ecc_inventory()
    print(f"Negotiating Curves... Using {curves['safe'][0]}")