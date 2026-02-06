def start_hybrid_tunnel():
    # [Low] 名單演算法：X25519_MLKEM768
    kex_mode = "X25519_MLKEM768"
    
    # [Low] 名單演算法：Frodo976shake
    fallback_kex = "Frodo976shake"
    
    print(f"Establishing tunnel with {kex_mode}...")
    print(f"Backup KEX set to {fallback_kex}")

if __name__ == "__main__":
    start_hybrid_tunnel()