from manimlib.imports import *
import math

class Advantages(Scene):
    def construct(self):
        #objects
        text1 = TextMobject("\\LARGE Rechengesetze:")
        text2 = TextMobject("1.", "Kommutativgesetz:")
        text3 = TextMobject("2.", "Assoziativgesetz:")
        text4 = TextMobject("3.", "Distributivgesetz: ")
        text5 = TextMobject("\\LARGE Beispiele: ")
        tex1 = TexMobject("a", #0
                          "+", #1
                          "b", #2
                          "=", #3
                          "b", #4
                          "+", #5
                          "a"   #6
                          )
        tex2 = TexMobject("a", #0
                          "+", #1
                          "(", #2
                          "b", #3
                          "+", #4
                          "c", #5
                          ")", #6
                          "=", #7
                          "(", #8
                          "a", #9
                          "+", #10
                          "b", #11
                          ")", #12
                          "+", #13
                          "c" #14
                          )
        tex3 = TexMobject("a",#0
                          "\\cdot",#1
                          "(",#2
                          "b",#3
                          "+",#4
                          "c",#5
                          ")",#6
                          "=",#7
                          "a",#8
                          "\\cdot",#9
                          "b",#10
                          "+",#11
                          "a",#12
                          "\\cdot",#13
                          "c"#14
                        )
        tex4 = TexMobject("1 \\frac{1}{4}", #0
                           "+2 \\frac{2}{3}", #1
                           "+1 \\frac{3}{4}", #2
                           "=",#3
                           )
        tex5 = TexMobject("1 \\frac{1}{4}", #0
                           "+1 \\frac{3}{4}", #1
                           "+2 \\frac{2}{3}", #2
                           )
        tex6 = TexMobject("=",#0
                           "3", #1
                           "+2 \\frac{2}{3}", #2
                           "=",#3
                           "5\\frac{2}{3}",#4
                            )
        #scene
        #Rechengesetze
        text1.set_color(BLUE)
        self.play(Write(text1))
        self.wait(1)
        self.play(ApplyMethod(text1.to_corner, UL))
        self.wait(1)
        #Kommutativgesetz
        self.play(Write(text2))
        self.play(ApplyMethod(text2.next_to,text1, DOWN *2))
        self.play(ApplyMethod(text2.shift,LEFT*0.35))
        self.wait(1)
        self.play(Write(tex1[0:4]))
        for letter,color in [("a",RED),("b",BLUE)]:
            tex1.set_color_by_tex(letter,color)
        self.wait(1)
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
        self.play(ApplyMethod(tex1.next_to, text2, RIGHT))
        #Assoziativgesetz
        self.play(Write(text3))
        self.wait()
        self.play(ApplyMethod(text3.next_to, text2, DOWN))
        self.play(ApplyMethod(text3.shift, LEFT*0.3))
        self.wait()
        self.play(Write(tex2[0:8]))
        for letter, color in [("(",RED), (")", RED)]:
            tex2.set_color_by_tex(letter,color)
        self.wait()
        changes_2 =[
            [(0,1,2,3,4,5,6),(9,10,8,11,13,14,12)]
            ]
        for pre_ind, post_ind in changes_2:
            self.play(
                *[
                    ReplacementTransform(tex2[i].copy(), tex2[j])
                    for i,j in zip(pre_ind, post_ind)
                    ]
                )  
        self.wait()
        self.play(ApplyMethod(tex2.next_to, text3, RIGHT))
        #Distributivgesetz
        self.play(Write(text4))
        self.wait
        self.play(ApplyMethod(text4.next_to, text3, DOWN))
        self.play(ApplyMethod(text4.shift,RIGHT*0.1))
        self.wait()
        self.play(Write(tex3[0:8]))
        for letter, color in [("a",RED), ("\\cdot",RED)]:
            tex3.set_color_by_tex(letter,color)
        changes_3 =[
            [(3,4,5),(10,11,14)],
            [(0,0,1,1),(8,12,9,13)]
            ]
        for pre_ind, post_ind in changes_3:
            self.play(
                *[
                    ReplacementTransform(tex3[i].copy(),tex3[j])
                    for i,j in zip(pre_ind, post_ind)
                    ]
                )
        self.wait()
        self.play(ApplyMethod(tex3.next_to, text4, RIGHT))
        self.wait(2)
        self.play(FadeOut(text1))
        self.remove(text3,text4,tex2,tex3)
        self.wait(1)
        #Transistion
        self.play(GrowFromCenter(text5))
        self.play(ApplyMethod(text5.to_corner, UL))
        #Example Kommutativgesetz
        tex4[1].set_color(RED)
        tex4[2].set_color(BLUE)
        tex5[2].set_color(BLUE)
        tex5[1].set_color(RED)
        self.play(Write(tex4[0:4]))
        self.play(ApplyMethod(tex4.shift, LEFT*4.8+UP*0.5))
        tex5.next_to(tex4,RIGHT, buff = 0.1)
        tex6.next_to(tex5,RIGHT, buff = 0.1)
        self.play(Write(tex5[0]))
        self.wait()
        changes_4=[
            [(1,2),(2,1)]
            ]
        self.add(tex4[3])
        for pre_ind, post_ind in changes_4:
            self.play(
                *[
                    ReplacementTransform(tex4[i].copy(),tex5[j])
                    for i,j in zip(pre_ind, post_ind)
                    ]
                )
        self.wait()
        tex5[0].set_color(YELLOW)
        tex5[1].set_color(YELLOW)
        tex5[2].set_color(WHITE)
        tex6[1].set_color(YELLOW)
        self.play(Write(tex6[0]))
        self.play(Write(tex6[2]))
        changes_5=[
            [(0,1),(1,1)]
            ]
        for pre_ind,post_ind in changes_5:
            self.play(
                *[
                    ReplacementTransform(tex5[i].copy(),tex6[j])
                    for i,j in zip(pre_ind, post_ind)
                    ]
                )
        self.play(Write(tex6[3]))
        self.wait()
        changes_6=[
            [(1,2),(4,4)]
            ]
        for pre_ind,post_ind in changes_6:
            self.play(
                *[
                    ReplacementTransform(tex6[i].copy(),tex6[j])
                    for i,j in zip(pre_ind, post_ind)
                    ]
                )
        self.wait(1)
        #Transition from exmaple Kommutativgesetz to example Assoziativgesetz
        text3.shift(0.75*UP+0.2*RIGHT)
        tex2.shift(0.75*UP+0.2*RIGHT)
        self.remove(tex1)
        self.play(FadeOut(tex4),run_time=0.1)
        self.play(FadeOut(tex5), run_time=0.1)
        self.play(FadeOut(tex6), run_time=0.1)
        self.play(FadeOut(text2))
        self.wait()
        self.play(FadeIn(text3))
        self.play(FadeIn(tex2))
        step1 = TexMobject("\\left(", #0
                           "\\frac{1}{2} +", #1
                           "\\frac{7}{4}", #2
                           "\\right)", #3
                           "+ \\frac{5}{4}", #4
                           "=", #5
                           )
        step2 = TexMobject("\\frac{1}{2} +", #0
                           "\\left(", #1
                           "\\frac{7}{4}", #2
                           "+ \\frac{5}{4}", #3
                           "\\right)", #4
                           "=", #5
                           )
        step3 = TexMobject("\\frac{1}{2} + ", #0
                           "3", #1
                           "=", #2
                           "3 \\frac{1}{2}", #3
                           )
        for letter, color in [("(",RED), (")",RED)]:
            step1.set_color_by_tex(letter,color)
            step2.set_color_by_tex(letter,color)
        self.play(ApplyMethod(step1.shift, LEFT*4.8+UP*0.5))
        step2.next_to(step1,RIGHT, buff = 0.1)
        step3.next_to(step2, RIGHT, buff = 0.1)
        self.wait()
        self.play(Write(step2[0]))
        self.play(Write(step2[2:4]))
        changes_7=[
            [(0,3),(1,4)]
            ]
        for pre_ind, post_ind in changes_7:
            self.play(
                *[
                    ReplacementTransform(step1[i].copy(),step2[j])
                    for i,j in zip(pre_ind, post_ind)
                    ]
                )
        self.wait()
        self.play(Write(step2[5]))
        self.play(Write(step3[0]))
        changes_8=[
            [(2,3),(1,1)]
            ]
        for pre_ind, post_ind in changes_8:
            self.play(
                *[
                    ReplacementTransform(step2[i].copy(),step3[j])
                    for i,j in zip(pre_ind, post_ind)
                    ]
                )
        self.wait()
        self.play(Write(step3[2]))
        changes_9=[
            [(0,1),(3,3)]
            ]
        for pre_ind, post_ind in changes_9:
            self.play(
                *[
                    ReplacementTransform(step3[i].copy(),step3[j])
                    for i,j in zip(pre_ind, post_ind)
                    ]
                )
        self.wait()
        
