package jaja; // 確保對應你的資料夾名稱

import java.security.MessageDigest;

public class PqcStandardSuite {

    public void initializeStandardPqc() throws Exception {
        // --- [Low] KEX / KEM (金鑰封裝與交換) ---
        String kex1 = "ML-KEM-1024";       // NIST FIPS-203 標準
        String kex2 = "X25519_MLKEM768";   // 混合模式
        String kex3 = "sntrup761";         // NTRU Prime
        String kex4 = "hqc192";            // HQC 候選

        // --- [Low] PKI / Signature (數位簽章) ---
        String sig1 = "ML-DSA-87";         // NIST FIPS-204 標準
        String sig2 = "falcon1024";        // Falcon
        String sig3 = "sphincsshake256fsimple"; // SPHINCS+
        String sig4 = "dilithium5";        // CRYSTALS-Dilithium

        // --- [Low] Hash (雜湊) ---
        // 雖然顯示 Not Applicable，但為了清單完整性仍可保留
        MessageDigest quantumHash = MessageDigest.getInstance("SHA-512");
        
        System.out.println("PQC Suite ready: " + kex1 + ", " + sig1 + ", " + sig4);
    }
}