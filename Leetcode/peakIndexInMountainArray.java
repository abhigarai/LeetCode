class Solution {
    public int peakIndexInMountainArray(int[] A) {
        int len=A.length;
        for(int i=0, j=len-1;i<len;i++,j--)
        {
            if(A[i+1]<A[i])
            {
                return i;
            }
            else if(A[j-1]<A[j]) {
                return j;
            }
        }
        return -1;
    }
}