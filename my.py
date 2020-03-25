from manimlib.imports import *
import math

class Advantages(Scene):
    def construct(self):
        
        #objects
        text1 = TextMobject("\\LARGE Rechenvorteile:")
        text2 = TextMobject("1.", "Kommutativgesetz:")
        text3 = TextMobject("2.", "Assoziativgesetz")
        tex1 = TexMobject("a", #0
                          "+", #1
                          "b", #2
                          "=", #3
                          "b", #4
                          "+", #5
                          "a"   #6
                          )
        tex2 = TexMobject("a",
                          "+",
                          "(",
                          "b",
                          "+",
                          "c",
                          ")",
                          )
        
        #scene
        #Rechenvorteile
        self.play(Write(text1))
        self.wait(1)
        text1.set_color(YELLOW)
        self.play(ApplyMethod(text1.to_corner, UL))
        self.wait(1)
        #Kommutativgesetz
        self.play(Write(text2))
        self.play(ApplyMethod(text2.next_to,text1, DOWN, buff=1))
        self.play(ApplyMethod(text2.shift,LEFT*0.35))
        self.wait(1)
        self.play(Write(tex1[0:4]))
        self.wait(1)
        for letter,color in [("a",RED),("b",BLUE)]:
            tex1.set_color_by_tex(letter,color)
        changes=[
            [(0,1,2),(4,5,6)]
            ]       
        for pre_ind, post_ind in changes:
            self.play(
                *[
                    ReplacementTransform(tex1[i].copy(), tex1[j])
                    for i,j in zip(pre_ind, post_ind)
                    ]
                )     
        self.wait()
        self.play(ApplyMethod(tex1.next_to, text2, RIGHT, buff=1))
        
        