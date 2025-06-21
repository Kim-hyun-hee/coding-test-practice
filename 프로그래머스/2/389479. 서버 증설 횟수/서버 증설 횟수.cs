using System;

public class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int[] server = new int[players.Length];

        for (int i = 0; i < players.Length; i++)
        {
            if (players[i] >= (server[i] + 1) * m)
            {
                int p = players[i] - server[i] * m;
                p = p / m;
                answer += p;
                for (int j = i; j < i + k; j++)
                {
                    if (j >= players.Length) break;
                    server[j] += p;
                }
            }
        }

        return answer;
    }
}