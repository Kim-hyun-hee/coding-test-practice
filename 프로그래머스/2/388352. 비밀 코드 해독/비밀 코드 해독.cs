using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int n, int[,] q, int[] ans)
        {
            int answer = 0;

            var list = new List<int>();
            for (int i = 1; i <= n; i++)
            {
                list.Add(i);
            }

            var c = Combinations(list, 5);
            foreach (var cc in c)
            {
                bool pass = true;
                for (int j = 0; j < q.GetLength(0); j++)
                {
                    int a = 0;
                    if (cc.Contains(q[j, 0])) a++;
                    if (cc.Contains(q[j, 1])) a++;
                    if (cc.Contains(q[j, 2])) a++;
                    if (cc.Contains(q[j, 3])) a++;
                    if (cc.Contains(q[j, 4])) a++;
                    if (ans[j] != a)
                    {
                        pass = false;
                        break;
                    }
                }
                if (pass) answer++;

            }

            return answer;
        }

        public IEnumerable<List<int>> Combinations(List<int> items, int r)
        {
            var queue = new Queue<(int start, List<int> current)>();
            queue.Enqueue((0, new List<int>()));

            while (queue.Count > 0)
            {
                var (start, current) = queue.Dequeue();
                if (current.Count == r)
                {
                    yield return current;
                    continue;
                }

                for (int i = start; i < items.Count; i++)
                {
                    var next = new List<int>(current) { items[i] };
                    queue.Enqueue((i + 1, next));
                }
            }
        }
}
