class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        char_counts = Counter(word)
        
        push =0 
        list1 = list(char_counts.values())
        list1.sort(reverse=True)
        for i in range(len(list1)) :
            push += (list1[i])*(i//8 +1)
        return push 


        
            



        