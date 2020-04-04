from manimlib.imports import *
import math

class asymptotes(GraphScene):
        CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -6,
        "y_max": 6,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE,
        "x_axis_width": 10,
        "y_axis_height":6
        }
        
        def construct(self):
            #objects
            label1 = TexMobject("\\frac{1}{x}")
            label1.shift(UP+2*RIGHT)
            label2 = TexMobject("\\frac{1}{x-1}")
            label2.shift(UP+3*RIGHT)
            #Make graph
            #Set 1
            self.setup_axes(animate=True)
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
        
class gebrrat10(GraphScene, Scene):
        CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -6,
        "y_max": 6,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE,
        "x_axis_width": 10,
        "y_axis_height":6
        }
        
        def construct(self):    
            #TextObjects
            
            tex1 = TexMobject("f(x)=", #0
                              "{", #1
                              "a", #2
                              "\\over", #3
                              "x", #4
                              "-", #5
                              "b", #6
                              "}", #7
                              "+", #8
                              "c" #9
                              )
            tex1[2].set_color(RED)
            tex1[6].set_color(YELLOW)
            tex1[9].set_color(GREEN)
                               
            tex2 = TexMobject("f(x)=", #0
                              "{", #1
                              "1", #2
                              "\\over", #3
                              "x", #4
                              "-",#5
                              "0", #6
                              "}", #7
                              "+", #8
                              "0" #9
                              )
            tex2[2].set_color(RED)
            tex2[6].set_color(YELLOW)
            tex2[9].set_color(GREEN)
            tex2.to_corner(UL)
            
            tex3 = TexMobject("f(x)=", #0
                              "{", #1
                              "1", #2
                              "\\over", #3
                              "x", #4
                              "-", #5
                              "2", #6
                              "}", #7
                              "+", #8
                              "0" #9
                              )
            tex3[2].set_color(RED)
            tex3[6].set_color(YELLOW)
            tex3[9].set_color(GREEN)
            tex3.to_corner(UL)
            
            tex4 = TexMobject("f(x)=", #0
                              "{", #1
                              "1", #2
                              "\\over", #3
                              "x", #4
                              "-", #5
                              "2", #6
                              "}", #7
                              "+", #8
                              "1,5" #9
                              )
            tex4[2].set_color(RED)
            tex4[6].set_color(YELLOW)
            tex4[9].set_color(GREEN)
            tex4.to_corner(UL)
            
            tex5 = TexMobject("f(x)=", #0
                              "{", #1
                              "2", #2
                              "\\over", #3
                              "x", #4
                              "-", #5
                              "2", #6
                              "}", #7
                              "+", #8
                              "1,5" #9
                              )
            tex5[2].set_color(RED)
            tex5[6].set_color(YELLOW)
            tex5[9].set_color(GREEN)
            tex5.to_corner(UL)
            
            label_y_asymptote1 = TexMobject("y =",
                                           "0")
            label_y_asymptote2 = TexMobject("y =",
                                           "1,5")
            label_y_asymptote1.to_edge(LEFT)
            label_y_asymptote2.to_edge(LEFT)
            label_y_asymptote1.set_color(GREEN)
            label_y_asymptote2.set_color(GREEN)
            label_y_asymptote2.shift(UP*0.75+LEFT*0.1)
            
            label_x_asymptote1 = TexMobject("x =",
                                           "0")
            label_x_asymptote2 = TexMobject("x =",
                                           "2")
            label_x_asymptote1.shift(RIGHT+DOWN)
            label_x_asymptote2.shift(RIGHT*2 + DOWN)
            label_x_asymptote1.set_color(YELLOW)
            label_x_asymptote2.set_color(YELLOW)
            
            #SceneIntro
            self.play(GrowFromCenter(tex1), run_time = 2)
            self.play(ApplyMethod(tex1.to_corner, UL))
            self.setup_axes(animate=True)
            ArrowAdder.AddArrows(self, self.x_max, self.y_max, self.axes_color)
            self.wait()
            #building graphs
            #graph1
            graph1p1=self.get_graph(self.func_to_graph,self.function_color, x_min=-10, x_max = -0.1)
            graph1p2=self.get_graph(self.func_to_graph, self.function_color, x_min =0.1, x_max=10)
            graph1 = VGroup(graph1p1, graph1p2)
            #graph2
            graph2p1=self.get_graph(self.func_to_graph2,self.function_color, x_min=-10, x_max = 1.9)
            graph2p2=self.get_graph(self.func_to_graph2, self.function_color, x_min =2.1, x_max=10)
            graph2 = VGroup(graph2p1, graph2p2)
            #grahp3
            graph3p1=self.get_graph(self.func_to_graph3, color = RED, x_min=-10, x_max = 1.9)
            graph3p2=self.get_graph(self.func_to_graph3,color = RED, x_min =2.1, x_max=10)
            graph3 = VGroup(graph3p1, graph3p2)
            #x_asymptote
            x_asymptotep1= self.get_vertical_line_to_graph(0.01, graph1p1, color = YELLOW)
            x_asymptotep1.shift(LEFT*0.01)
            x_asymptotep2 = self.get_vertical_line_to_graph(-0.1, graph1p1, color = YELLOW)
            x_asymptotep2.shift(RIGHT*0.05)
            x_asymptote= VGroup(x_asymptotep1, x_asymptotep2)
            #y_asymptote
            y_asymptote = self.get_graph(self.to_y_asymptote, color = GREEN, x_min = -10, x_max =10)
            
            #Playing Scene
            self.play(ReplacementTransform(tex1, tex2))
            self.wait()
            self.play(ShowCreation(graph1))
            self.wait()
            self.play(ShowCreation(y_asymptote))
            self.play(Write(label_y_asymptote1))
            self.wait()
            self.play(ShowCreation(x_asymptote), run_time=0.1)
            self.play(Write(label_x_asymptote1))
            self.wait(3)
            self.play(WiggleOutThenIn(tex2[6], scale_value = 2))
            self.play(ReplacementTransform(tex2, tex3))
            self.play(WiggleOutThenIn(tex3[5], scale_value=3))
            self.wait()
            self.play(ReplacementTransform(graph1, graph2), ApplyMethod(x_asymptote.shift,RIGHT), ReplacementTransform(label_x_asymptote1, label_x_asymptote2))
            self.wait(3)
            self.play(WiggleOutThenIn(tex3[9], scale_value = 2))
            self.play(ReplacementTransform(tex3, tex4))
            self.play(WiggleOutThenIn(tex3[8], scale_value=3))
            self.wait()
            self.play(ApplyMethod(graph2.shift,UP*0.75), ApplyMethod(y_asymptote.shift, UP*0.75), ReplacementTransform(label_y_asymptote1, label_y_asymptote2))
            self.wait(3)
            self.play(WiggleOutThenIn(tex4[2]))
            self.play(ReplacementTransform(tex4, tex5))
            self.wait()
            self.play(ReplacementTransform(graph2, graph3))
            self.wait(3)
            
            
            
            
        def func_to_graph(self,x):
            return (1/x)
        
        def func_to_graph2(self,x):
            return (1/(x-2))
        
        def func_to_graph3(self,x):
            return(2/(x-2) + 1.5)
        
        def to_y_asymptote(self,x):
            return (0)
        
class PlotGraph(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 20,
        "x_max" : 7,
        "x_min" : 4,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
        "axes_color" : BLUE,
        "y_labeled_nums": range(30,60,10),
        "x_labeled_nums": list(np.arange(4, 7.0+0.5, 0.5)),
        "x_label_decimal":1,
        "graph_origin": 3 * DOWN + 6 * LEFT,
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,
        "x_axis_label": None,
        "x_axis_width":10
    }

    def construct(self):
        self.setup_axes(animate=False) #animate=True to add animation
        self.x_axis.shift(LEFT*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        self.y_axis.shift(DOWN*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        self.y_axis_label_mob.next_to(self.y_axis[0].get_end(),UP)
        p=Dot().move_to(self.coords_to_point(self.x_min, self.y_min))
        self.add(p)
        graph = self.get_graph(lambda x : x**2, 
                                    color = GREEN,
                                    x_min = 5, 
                                    x_max = 7
                                    )

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()  
        