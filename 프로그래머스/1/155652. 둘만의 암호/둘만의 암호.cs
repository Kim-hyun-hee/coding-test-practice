using System;
using System.Linq;

public class Solution {
    public string solution(string s, string skip, int index) {
        string remain = new string("abcdefghijklmnopqrstuvwxyz".Where(x => !skip.Contains(x)).ToArray());
        var answer = string.Empty;
    
        foreach (var c in s)
        {
            int i = (remain.IndexOf(c) + index) % remain.Length;
            answer += remain[i];
        }
    
        return answer;
    }
}