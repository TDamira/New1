class Box:
     def __init__(self, width, height):
        self.width=width
        self.height=height
     def square(self):
         print(f"square: {self.width*self.height}")

box=Box(10,20)
box.square()