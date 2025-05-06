public class Main {

    public static void main(String[] args) {
        int[] array = {8, 2, 5, 3, 9, 4, 7, 6, 1};

        quickSort(array, 0, array.length - 1);
        
                for (int i : array) {
                    System.out.print(i + " ");
                }
            }
        
            private static void quickSort(int[] array, int start, int end) {
                
                if (end <= start) return;   // Base case

                // Partition array at the pivot
                int pivot = partition(array, start, end);
                // left side of the pivot
                quickSort(array, start, pivot - 1);
                // right side of the pivot
                quickSort(array, pivot + 1, end);
            }
            private static int partition(int[] array, int start, int end) {
                // Pivot is the value at end of array
                int pivot = array[end];

                int i = start - 1;

                for (int j = start; j <= end - 1; j++){
                    // if value at j is less than the pivot swap i and j
                    if(array[j] < pivot){
                        i++;
                        int temp = array[i];
                        array[i] = array[j];
                        array[j] = temp;
                    }
                }
                // Increment i then swap i with the pivot to place at correct spot
                i++;
                int temp = array[i];
                array[i] = array[end];
                array[end] = temp;

                // Return the location of the pivot
                return i;
                
            }
            
}