public class KthlargestElement {
    public static void main(String[] args) {
        int[] arr = {1,23,4,51,6,55};
        int max =  Integer.MIN_VALUE;
        int k = 2; 
      
        for (int i = 0; i < arr.length; i++) {

            
            for (int j = i + 1; j < arr.length; j++) {

                
                int temp = 0;
                if (arr[j] < arr[i]) {

                    
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }

        }
        for (int i = 0; i < arr.length; i++) {
            if(arr.length+1-i == k){
                System.out.println("The " + k + "th largest element is: " + arr[i]);
                break;
        }
    }}
}
