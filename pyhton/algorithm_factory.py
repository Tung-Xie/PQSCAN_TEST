import hashlib
import json

class PqcAlgorithmFactory:
    def __init__(self):
        # 你的 PQC 大名單字典
        self.supported_pqc = {
            "KEM": ["ML-KEM-1024", "X25519_MLKEM768", "sntrup761", "hqc256", "frodo1344shake"],
            "SIG": ["ML-DSA-87", "falcon1024", "dilithium5", "sphincsshake256fsimple"],
            "ECC": ["secp256r1", "x25519", "p384_kyber768"]
        }

    def create_key_pair(self, algo_name):
        """模擬 Key Generation 呼叫"""
        if algo_name in self.supported_pqc["KEM"] or algo_name in self.supported_pqc["SIG"]:
            print(f"[Crypto-Function] Generating KeyPair for Algorithm: {algo_name}")
            return f"PUB_KEY_{algo_name}", f"PRIV_KEY_{algo_name}"
        raise ValueError("Unsupported Algorithm")

    def perform_signature(self, algo_name, message):
        """模擬 Digital Signature 呼叫"""
        print(f"[Crypto-Function] Signing message using: {algo_name}")
        # 模擬呼叫行為
        return f"SIG_DATA_VIA_{algo_name}"

    def establish_secure_tunnel(self, hybrid_algo):
        """模擬 KEX / Hybrid Mode 呼叫"""
        print(f"[Crypto-Function] Establishing Hybrid KEX tunnel: {hybrid_algo}")
        return "SHARED_SECRET"

# --- 實際執行呼叫 (這才是關鍵) ---
def run_pqc_demo():
    factory = PqcAlgorithmFactory()
    
    # 1. 呼叫 KEM (包含混合模式)
    factory.create_key_pair("ML-KEM-1024")
    factory.establish_secure_tunnel("X25519_MLKEM768")
    factory.establish_secure_tunnel("p384_kyber768")

    # 2. 呼叫 Signature
    factory.perform_signature("ML-DSA-87", "Tony_Auth_Message")
    factory.perform_signature("falcon1024", "System_Log_Data")

    # 3. 呼叫 Hash (包含你要求的 SHA-384/512)
    data = b"Quantum_Safe_Test"
    h1 = hashlib.sha512(data).hexdigest()
    h2 = hashlib.sha3_512(data).hexdigest()

if __name__ == "__main__":
    run_pqc_demo()