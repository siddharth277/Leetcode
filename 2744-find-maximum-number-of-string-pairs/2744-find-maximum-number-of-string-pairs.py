class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        def ispal (word1 , word2):
            return word1 == word2[::-1]
        count =0
        for i in range (len(words)):
            for j in range(i+1 , len(words)):
                if ispal(words[i],words[j]):
                    count+=1
        return count
        
        