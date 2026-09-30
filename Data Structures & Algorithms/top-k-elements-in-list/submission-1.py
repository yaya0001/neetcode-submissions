class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #y=Counter(nums)
        #return list(dict(y.most_common(k)).keys())
        counterdict= defaultdict(int)
        for i in nums:
            counterdict[i]+=1
        common=sorted(counterdict.items(),key=lambda a:a[1],          reverse=True)[:k]
        return [key for key,value in common]