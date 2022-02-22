
class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sq_sum(self):
        x = self.x **2 # self.x * self.x
        z = self.z * self.z # self.z**3 -> self.z*self.z*self.z
        y = self.y * self.y
        return  x +z +y


point = Point(1,3,5)
print(point.sq_sum())