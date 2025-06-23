using System;
using System.Linq;

public class Solution {
    public string solution(string s, string skip, int index) {
        string alphabet = "abcdefghijklmnopqrstuvwxyz";
        string remain = string.Empty;

        foreach (char c in alphabet)
        {
            if (!skip.Contains(c))
            {
                remain += c;
            }
        }

        string answer = string.Empty;

        foreach (char c in s)
        {
            int i = (remain.IndexOf(c) + index) % remain.Length;
            answer += remain[i];
        }

        return answer;
    }
}