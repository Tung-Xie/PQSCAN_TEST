

import java.security.*;

public class LegacySecurity {
    public void oldSystem() throws Exception {
        // [Critical] 極易被破解
        String curve1 = "secp160k1"; 
        String curve2 = "secp192r1";
        KeyPairGenerator rsaOld = KeyPairGenerator.getInstance("RSA");
        rsaOld.initialize(1024); // RSA < 2048 是 Critical

        // [Critical] Hash 漏洞
        MessageDigest md5 = MessageDigest.getInstance("MD5");

        // [High] 已被標準棄用
        String dsa = "DSA";
        MessageDigest sha1 = MessageDigest.getInstance("SHA-1");

        System.out.println("Using legacy: " + curve1 + ", " + md5.getAlgorithm());
    }
}