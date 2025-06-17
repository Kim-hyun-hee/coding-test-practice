using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int[] solution(int n)
    {
        int[,] arr = new int[n, n];
        int[,] dir = { { 0, 1 }, { 1, 0 }, { -1, -1 } };

        int x = 0;
        int y = 0;
        int d = 0;
        int i = 1;

        while (true)
        {
            arr[x, y] = i++;
            if (i == n * (n + 1) / 2 + 1)
                break;

            int new_x = x + dir[d, 0];
            int new_y = y + dir[d, 1];

            if (new_x >= n || new_y >= n || arr[new_x, new_y] != 0)
            {
                d = (d + 1) % 3;
                x += dir[d, 0];
                y += dir[d, 1];
            }
            else
            {
                x = new_x;
                y = new_y;
            }
        }

        List<int> answer = new List<int>();
        for (i = 0; i < n; i++)
        {
            for (int j = 0; j <= i; j++)
            {
                answer.Add(arr[j, i]);
            }
        }

        return answer.ToArray();
    }
}
