using System;

public class Solution {
    public int solution(int n, int w, int num) {
        
        int t = (n / w + 1) * w;
        int[] arr = new int[t];
        int i = 0;
        int a = 1;

        for (i = 0; i < t / w; i++)
        {
            if (i % 2 == 0)
            {
                for (int j = i * w; j < (i + 1) * w; j++)
                {
                    arr[j] = a++;
                }
            }
            else
            {
                for (int j = (i + 1) * w - 1; j >= i * w; j--)
                {
                    arr[j] = a++;
                }
            }
        }

        int index = Array.IndexOf(arr, num);
        int answer = 0;
        
        for (i = index; i < t; i += w)
        {
            if (arr[i] > n) break;
            answer++;
        }
        
        return answer;
    }
}