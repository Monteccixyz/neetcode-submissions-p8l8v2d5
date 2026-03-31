class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pairs = {}
        for n in nums:
            if n in pairs:
                pairs[n] += 1
            else:
                pairs[n] = 1
        return [tup[0] for tup in sorted(pairs.items(), key=lambda x: x[1])[-k:]]