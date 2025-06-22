using System;
using System.Linq;

public class Solution {
    public int solution(int n, int[,] q, int[] ans) {
        int result = 0;

        int[] compare;
        for(int i = 0; i < n - 4; i++) {
            for(int j = i + 1; j < n - 3; j++) {
                for(int k = j + 1; k < n - 2; k++) {
                    for(int l = k + 1; l < n - 1; l++) {
                        for(int m = l + 1; m < n; m++) {
                            compare = new int[] { i + 1, j + 1, k + 1, l + 1, m + 1 };

                            bool isClear = true;
                            for(int a = 0; a < q.GetLength(0); a++) {
                                int answer = ans[a];

                                int count = 0;
                                for(int b = 0; b < 5; b++) {
                                    if(compare.Contains(q[a, b])) {
                                        count++;
                                    }
                                }

                                if(answer != count) {
                                    isClear = false;

                                    break;
                                }
                            }

                            if(isClear) {
                                result++;
                            }
                        }
                    }
                }
            }
        }

        return result;
    }
}