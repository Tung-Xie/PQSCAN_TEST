

public class AdvancedPkiService {
    public void setupPki() {
        // --- ECDSA 相關 (傳統加密) ---
        // [Medium] 主流安全曲線
        String ecc1 = "ecdsa_secp256r1_sha256"; 
        String ecc2 = "ecdsa_secp384r1_sha384";
        
        // [Critical] 極度危險的 ECDSA (160-bit)
        String eccOld = "secp160r1"; 

        // --- PQC 簽章替代方案 (NIST FIPS-204) ---
        // [Low] 數位簽章
        String pqcSig1 = "ML-DSA-65";
        String pqcSig2 = "falcon1024";
        String pqcSig3 = "dilithium3";

        System.out.println("PKI Assets Loaded: " + ecc1 + " and " + pqcSig1);
    }
}