public class ThreeSumOptimization {
    public static void main(String[] args) {
        int[] nums = {-1, 0, 1, 2, -1, -4};
         int i = 0 , j = 1 , k = 3 ;
            while (i < nums.length) {

                if( j == nums.length || k == nums.length) {
                    break;}
                if (nums[i] + nums[j] + nums[k] == 0) {
                    System.out.println(nums[i] + " " + nums[j] + " " + nums[k]);
                    
                }
               
            }
    }
}
