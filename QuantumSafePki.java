

public class QuantumSafePki {
    public void deployPqcPki() {
        // [Low] NIST FIPS-204 標準 (ML-DSA)
        String sig1 = "ML-DSA-44";
        String sig2 = "ML-DSA-65";
        String sig3 = "ML-DSA-87";

        // [Low] 其他 PQC 簽章
        String sig4 = "falcon512";
        String sig5 = "falcon1024";
        String sig6 = "sphincsshake256fsimple";
        String sig7 = "dilithium3";

        // [Low] 其他名單算法
        String sig8 = "mayo1";
        String sig9 = "snova2454";

        System.out.println("Signature Assets: " + sig1 + ", " + sig4 + ", " + sig8);
    }
}