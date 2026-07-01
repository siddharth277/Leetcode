class Solution:
    def validSquare(self, p1, p2, p3, p4):

        def distance(a, b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2

        d = [
            distance(p1,p2),
            distance(p1,p3),
            distance(p1,p4),
            distance(p2,p3),
            distance(p2,p4),
            distance(p3,p4)
        ]

        d.sort()

        return d[0] > 0 and \
               d[0]==d[1]==d[2]==d[3] and \
               d[4]==d[5]