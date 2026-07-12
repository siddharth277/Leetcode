class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        p = ord(coordinates[0])
        return not (p+int(coordinates[1]))%2==0

        
        