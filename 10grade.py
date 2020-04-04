from manimlib.imports import *
import math

class asymptotes(GraphScene, Scene):
        CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -6,
        "y_max": 6,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE,
        "x_axis_width": 10,
        "y_axis_height":6,
        "include_tip": True
        }
        
        def construct(self):
            #objects
            label1 = TexMobject("\\frac{1}{x}")
            label1.shift(UP+2*RIGHT)
            label2 = TexMobject("\\frac{1}{x-1}")
            label2.shift(UP+3*RIGHT)
            #Make graph
            #Set 1
            self.setup_axes(animate = True)
            n1 = NumberLine(x_min = 4.5, x_max = 5.5, color = BLUE, include_tip = True, tip_width = 0.15, tip_height = 0.15)
            n2 = NumberLine(x_min = -0.5, x_max = 0.5, color = BLUE, include_tip = True, tip_width = 0.15, tip_height = 0.15)
            n2.rotate(90*DEGREES)
            n2.shift(UP*3)
            self.play(ShowCreation(n1),ShowCreation(n2), run_time = 0.1)
            
            func_graph=self.get_graph(self.func_to_graph,self.function_color, x_min=-14, x_max = -0.1)
            func_graph2=self.get_graph(self.func_to_graph,self.function_color, x_min=0.1, x_max = 14)
            vert_line= self.get_vertical_line_to_graph(0.01, func_graph, color = YELLOW)
            vert_line.shift(LEFT*0.01)
            vert_line2 = self.get_vertical_line_to_graph(-0.1, func_graph, color = YELLOW)
            vert_line2.shift(RIGHT*0.05)
            func_graph3=self.get_graph(self.func_to_graph_2, color = YELLOW, x_min=-14, x_max =14)
            #Set2
            vertline = VGroup(vert_line, vert_line2)
            graph = VGroup(func_graph, func_graph2)
            everything = VGroup(graph, vertline, func_graph3)
            #Display graph
            self.play(ShowCreation(func_graph))
            self.play(ShowCreation(func_graph2))
            self.play(Write(label1))
            self.wait(1)
            self.play(ShowCreation(vertline), run_time =0.01)
            self.wait(2)
            self.play(ShowCreation(func_graph3))
            self.wait(2)
            self.play(ApplyMethod(everything.shift,RIGHT*0.5), Transform(label1, label2))
            self.wait(2)
    
    
        def func_to_graph(self, x):
            return (1/x)
    
        def func_to_graph_2(self, x):
            return(0)
        
        def func_to_graph_3(self, x):
            return (1/(x-1))
        
class test(GraphScene):
     def construct(self):
        n1 = NumberLine(x_min = -2, x_max = 2, color = BLUE, include_tip = True)
        n2 = NumberLine(x_min = -2, x_max = 2)
        n2.rotate(90*DEGREES)
        self.play(ShowCreation(n1))
        self.play(ShowCreation(n2))
        