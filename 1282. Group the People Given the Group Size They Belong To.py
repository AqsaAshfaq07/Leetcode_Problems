class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # n people 
        # ids -> 0 - n-1
        # groupSizes -> 

        n = len(groupSizes)
        ans = []
        sz_to_group = {}
        
        for i in range(n):
            if groupSizes[i] not in sz_to_group:
                sz_to_group[groupSizes[i]] = []    

            group = sz_to_group[groupSizes[i]]
            group.append(i)
            
            # When the list size equals the group size, empty it and store it in the answer.
            if len(group) == groupSizes[i]:
                ans.append(group)
                del sz_to_group[groupSizes[i]]
        
        return ans