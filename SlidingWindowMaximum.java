class SlidingWindowMaximum{
    public static void main(String[] args) {
        int[] arr = {1,3,-1,-3,5,3,6,7};
        int  k = 3 ;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < j+3; j+= 3) {
                if(arr[j] > max){
                    max = arr[j];
                   
                    
                 }System.out.println(max+ " ");
            if(j+3 > arr.length){ break;}}
        
    }
}
}