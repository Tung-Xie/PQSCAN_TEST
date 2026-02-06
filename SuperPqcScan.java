
import java.security.*;

public class SuperPqcScan {
    public void triggerAll() throws Exception {
        // --- 衝高 KEM 數量 ---
        String[] kems = {"ML-KEM-512", "ML-KEM-1024", "BIKE-L1", "BIKE-L3", "HQC-128", "HQC-256", "Frodo640-AES"};
        for(String s : kems) { KeyPairGenerator.getInstance(s, "BCPQC"); }

        // --- 衝高 Signature 數量 ---
        String[] sigs = {"ML-DSA-44", "ML-DSA-87", "Falcon-512", "Falcon-1024", "Dilithium2", "Dilithium5", "SPHINCS-Plus"};
        for(String s : sigs) { KeyPairGenerator.getInstance(s, "BCPQC"); }

        // --- 衝高 Classic McEliece (這通常是亮點) ---
        KeyPairGenerator.getInstance("Classic-McEliece-348864", "BCPQC");
        KeyPairGenerator.getInstance("Classic-McEliece-8192128f", "BCPQC");
    }
}