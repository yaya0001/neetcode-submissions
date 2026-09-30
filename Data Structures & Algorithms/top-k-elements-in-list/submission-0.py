class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        y=Counter(nums)
        return list(dict(y.most_common(k)).keys())