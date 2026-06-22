class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)

        for i in range(n, 0, -1):
            for j in range(n):
                if arr[j] == i:
                  
                    for k in range((j + 1) // 2):
                        arr[k], arr[j - k] = arr[j - k], arr[k]

                    for k in range(i // 2):
                        arr[k], arr[i - k - 1] = arr[i - k - 1], arr[k]

                    ans.append(j + 1)
                    ans.append(i)
                    break

        return ans