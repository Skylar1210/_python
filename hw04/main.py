class shapes(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        pass
    sum=0

class rectangle(shapes):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height



class square(rectangle):

    def __init__(self,width):
        self.width=width
        self.height=width

class ellipse(rectangle):

    def __init__(self,width,length):
        self.width=width
        self.height=length*3.14

class circle(rectangle):

    def __init__(self,width):
        self.width=width
        self.height=width*3.14
        
        
shapes = [ellipse(10, 20), square(15), circle(5),rectangle(20, 15), circle(5), square(15),ellipse(10, 20)]        
compute_area=[x.area for x in shapes]
total_area=sum(compute_area)
