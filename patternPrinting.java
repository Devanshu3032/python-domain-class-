public class patternPrinting {
    public static void main(String[] args) {
        int n = 9;
        for (int i = n; i >0; i--) {
            for (int j = i; j > 0; j--) {
                System.out.print((char)(i+64) +" " );
                
            }
            System.out.println();
        }
    }
    
}
