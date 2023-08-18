class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
    # n cities -> roads [] -> [a, b] -> bidirectional road exists between a and b
    # network rank - total no. of directly connected roads

        city_rank = [0] * n
        connections = set()
        for road in roads:
            connections.add(tuple(road))
            city_rank[road[0]] += 1
            city_rank[road[1]] += 1

        max_rank = 0

        for i in range(n):
            for j in range(i+1, n):
                rank = city_rank[i] + city_rank[j]

                if (i, j) in connections or (j, i) in connections:
                    rank -= 1

                max_rank = max(rank, max_rank)

        return max_rank