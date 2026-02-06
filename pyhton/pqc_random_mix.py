import hashlib

def crypto_mix_bench():
    # --- [Low] PQC 區 ---
    pqc_assets = {
        "KEX": "Frodo640aes", 
        "Signature": "falcon1024",
        "KEM": "kyber1024",
        "Hybrid": "sntrup761x25519-sha512@openssh.com"
    }

    # --- [Medium] 主流區 ---
    mainstream = ["x448", "ed25519", "sha256"]

    # --- [Critical/High] 測試區 (如果你想看紅燈，取消註解這行) ---
    # legacy = "MD5" 

    # [Crypto Function] Digest
    # 使用 SHA-512 (Low Risk)
    m = hashlib.sha512()
    print(f"Running PQC assets: {pqc_assets}")