class SuperiorarrayElement{
    public static void main(String[] args) {
        int[] arr = {2,8,9,7,4,2};
        int max = 0  ;
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if( i == arr.length-1){ count++; break;}
             if(arr[i]>arr[i+1]){ max = arr[i];
            count++ ;}

        }

        System.out.print(count);
    }
}