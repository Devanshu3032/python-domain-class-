class indexValue{
    public static void main(String[] args) {
        int[] arr = {4,5,6,7,0,1,2};
        int target = 0;
        int countt = 0;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] == target) {
                System.out.println("Index of " + target + " is: " + i);
                
            }
           
            
        }
        if( countt == 0 ){System.out.println("-1");}
    } 
}