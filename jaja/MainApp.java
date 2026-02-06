package jaja;

public class MainApp {
    public static void main(String[] args) {
        PqcKeyExchange kex = new PqcKeyExchange();
        PqcSignatureService sig = new PqcSignatureService();
        
        // 實際執行 (Call Functions)
        kex.performKEM();
        sig.signDocument();
    }
}