import math
#create a class Point2D in two-dimensional space
class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def say(self):
        print("My location is (%d"%self.x+",%d)"%self.y)
        
#create a class Point3D derived from Point2D in three-dimensional space 
class Point3D(Point2D):
    def __init__(self,x,y,z):
        Point2D.__init__(self,x,y)
        self.z = z
    def say(self):#override the say() Method
        print("My location is (%d"%self.x+",%d"%self.y+",%d)"%self.z)
        
#getDistancefor2Points calculates the distance P1-->P2
#sqrt((X1-X2)^2+(y1-y2)^2))
def getDistancefor2Points(p1,p2):
    xdiff = p1.x - p2.x
    ydiff = p1.y - p2.y
    d = math.sqrt(pow(xdiff,2) + pow(ydiff,2))
    return d

if __name__ == "__main__":
    p1 = Point2D(10,10)
    p1.say()
    p2 = Point3D(100,100,100)
    p2.say() # Point3D doesn't has say() Method,so p2 use Point2D say()Method
    p3 = Point2D(50,10)
    p3.say()
    print(getDistancefor2Points(p1,p3))


