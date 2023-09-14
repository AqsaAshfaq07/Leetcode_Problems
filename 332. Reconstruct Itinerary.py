class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    # airline tickets -> tickets[i] = [from, to]
    # tickets shows the departure and arrival airports of one flight. 
    # --> sort the tickets array in lexcial order

        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]
        