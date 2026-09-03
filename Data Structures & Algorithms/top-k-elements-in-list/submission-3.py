class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        freq = [[] for i in range(len(nums)+1)]

        for num, frq in count.items():
            freq[frq].append(num)

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 


        

        