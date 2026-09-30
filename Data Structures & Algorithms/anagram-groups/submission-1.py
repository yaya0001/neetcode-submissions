class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x=defaultdict(list)
        for i in strs:
            key=tuple(sorted(Counter(i).items()))
            x[key].append(i)
        return list(x.values())

