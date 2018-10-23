class shapes(object):

    @property
    def area(self):
        pass

    
class rectangle(shapes):
    def __init__(self,width=0,height=0):
        super().__init__()
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width*self.height



class square(rectangle):

    def __init__(self,width=0):
        super().__init__()
        self.width=width
        self.height=width

class ellipse(rectangle):

    def __init__(self,width=0,height=0):
        super().__init__()
        self.width=width
        self.height=height*3.14

class circle(rectangle):

    def __init__(self,width=0):
        super().__init__()
        self.width=width
        self.height=width*3.14


        
        
shapes = [ellipse(10, 20), square(15), circle(5),rectangle(20, 15), circle(5), square(15),ellipse(10, 20)]        
compute_area=[x.area for x in shapes]
print（compute_area）
total_area=sum(compute_area)
print(total_area)
