class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
       
        if sentence[0] != sentence[len(sentence)-1]:
            return False
        for i in range(len(sentence)-1):
            if sentence[i+1] == " ":
                if sentence[i] != sentence[i+2]:
                    return False
        return True


        