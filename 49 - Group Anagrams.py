class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        anagarm_groups = collections.defaultdict(list)

        for str_ in strs:
            sorted_str = "".join(sorted(str_))
            anagarm_groups[sorted_str].append(str_)

        return anagarm_groups.values() 