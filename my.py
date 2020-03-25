from manimlib.imports import *
import math

class BigTest(Scene):
    def construct(self):
        #object declaration
        dot1 = Dot()
        dot2 = Dot()
        circle = Circle(color = RED_E)
        square = Square()
        rectangle = Rectangle()
        triangle = Triangle()
        tex=TexMobject(r"\frac{a^2}{b^2} + \int_0^3 f^2(x) dx")
        text = TextMobject("H","a","l","l","o!")
        grid = ScreenGrid()

        #color setting
        #for i in[0,1,3,4]:
        #    text[i].set_color(RED)
        for i in range(3,5):
            text[i].set_color(RED)    
        #moving objects in start position
        dot1.to_corner(UR)
        dot2.to_corner(UL)
        circle.to_corner(DR)
        square.to_corner(DL)
        triangle.to_edge(UP)
        tex.to_edge(LEFT)
        text.to_edge(DOWN)

        #starting 
        self.add(dot1,dot2,circle,square,triangle,tex,text,grid)
        self.wait(4)
        text[0].shift(2*UP)
        self.wait(1)
        text[1].shift(2*UP)
        self.wait(1)
        self.play(Transform(text[0], text[1]))
        self.wait(4)
        
