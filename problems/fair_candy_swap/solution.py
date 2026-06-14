class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = sum(aliceSizes) - sum(bobSizes)
        half_diff = diff // 2
        alice_set, bob_set = set(aliceSizes), set(bobSizes)
        for a in alice_set:
            if a - half_diff in bob_set:
                return [a, a - half_diff]