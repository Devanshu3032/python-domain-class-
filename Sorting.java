public class Sorting {
    public void sortColors(int[] nums) {
        int zeroIndex = 0;
        int twoIndex = nums.length - 1;
        int i = 0;

        while (i <= twoIndex) {
            if (nums[i] == 0) {
                swap(nums, i, zeroIndex);
                zeroIndex++;
                i++;
            } else if (nums[i] == 2) {
                swap(nums, i, twoIndex);
                twoIndex--;
            } else {
                i++;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void main(String[] args) {
        Sorting0,1And2 solution = new Sorting0,1And2();
        int[] nums = {2,0,2,1,1,0};
        solution.sortColors(nums);
        for (int num : nums) {
            System.out.print(num + " ");
        }
    }
    
}
