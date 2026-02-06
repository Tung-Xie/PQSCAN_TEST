

import javax.crypto.Cipher;

public class BlockCipherVault {
    public void initCiphers() throws Exception {
        // --- Block Ciphers ---
        // [Medium] 目前最安全
        Cipher aes = Cipher.getInstance("AES/CBC/PKCS5Padding");
        
        // [High/Critical] 模擬舊型塊加密
        String oldCipher = "DESede"; // 3DES
        String badCipher = "DES";    // 完全不安全

        // --- PQC 輔助加密字串 (KEM) ---
        // [Low] NIST 標準
        String pqcKem = "ML-KEM-1024";
        String pqcMcEliece = "Classic-McEliece-460896f";

        System.out.println("Block Ciphers and PQC KEM Ready.");
    }
}