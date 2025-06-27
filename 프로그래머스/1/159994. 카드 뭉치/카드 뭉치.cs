using System;

public class Solution {
    public string solution(string[] cards1, string[] cards2, string[] goal) {
        int i = 0;
        int j = 0;

        for (int k = 0; k < goal.Length; k++)
        {
            if (i < cards1.Length && cards1[i] == goal[k])
            {
                i++;
            }
            else if (j < cards2.Length && cards2[j] == goal[k])
            {
                j++;
            }
            else
            {
                return "No";
            }
        }

        return "Yes";
    }
}