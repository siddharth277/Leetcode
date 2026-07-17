class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard=['qwertyuiop','asdfghjkl','zxcvbnm']
        result=[]
        for word in words:
            row1,row2,row3=0,0,0
            for x in word:
                if x.lower() in keyboard[0]:
                    row1+=1
                elif x.lower() in keyboard[1]:
                    row2+=1
                elif x.lower() in keyboard[2]:
                    row3+=1
            if row1==len(word) or row2==len(word) or row3==len(word):
                result.append(word)   
        return result                     


        