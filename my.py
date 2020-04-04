from manimlib.imports import *
import math

def changer(self,changes, object1, object2):
        for pre_ind, post_ind in changes:
            self.play(
                *[
                    ReplacementTransform(object1[i].copy(),object2[j])
                    for i,j in zip(pre_ind, post_ind)
                    ]
                )


class Advantages(Scene):
    def construct(self):
        #objects
        #helpers
        #texts
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
        tex7 = TexMobject("\\left(", #0
                           "\\frac{1}{2} +", #1
                           "\\frac{7}{4}", #2
                           "\\right)", #3
                           "+ \\frac{5}{4}", #4
                           "=", #5
                           )
        tex8 = TexMobject("\\frac{1}{2} +", #0
                           "\\left(", #1
                           "\\frac{7}{4}", #2
                           "+ \\frac{5}{4}", #3
                           "\\right)", #4
                           "=", #5
                           )
        tex9 = TexMobject("\\frac{1}{2} + ", #0
                           "3", #1
                           "=", #2
                           "3 \\frac{1}{2}", #3
                           )
        step1 = TexMobject("\\left(",# 0
                           "\\frac{7}{3}", #1
                           "+\\frac{5}{6}", #2
                           "\\right)", #3
                           "\\cdot 6", #4
                           "=", #5
                           )
        step2 = TexMobject("\\frac{7}{3}", #0
                           "\\cdot 6", #1
                           "+\\frac{5}{6}", #2
                           "\\cdot 6",#3
                           "=", #4
                           )
        step3 = TexMobject("14", #0
                           "+", #1
                           "5", #2
                           "=", #3
                           "19", #4
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
        ChangeTransform.changer(self,changes,tex1,tex1)   
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
        ChangeTransform.changer(self,changes_2,tex2,tex2)
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
        ChangeTransform.changer(self,changes_3,tex3,tex3)
        self.wait()
        self.play(ApplyMethod(tex3.next_to, text4, RIGHT))
        self.wait(2)
        self.play(FadeOut(text1))
        self.play(FadeOut(text3),run_time=0.1)
        self.play(FadeOut(text4), run_time=0.1)
        self.play(FadeOut(tex2), run_time=0.1)
        self.play(FadeOut(tex3), run_time=0.1)
        self.remove(text3,text4,tex2,tex3)
        self.wait(1)
        #Transistion
        self.play(GrowFromCenter(text5))
        self.play(ApplyMethod(text5.to_corner, UL))
        #Example Kommutativgesetz
        tex4[1].set_color(RED)
        tex4[2].set_color(BLUE)
        tex5[1].set_color(BLUE)
        tex5[2].set_color(RED)
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
        ChangeTransform.changer(self,changes_4,tex4,tex5)
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
        ChangeTransform.changer(self,changes_5,tex5,tex6)
        self.play(Write(tex6[3]))
        self.wait()
        changes_6=[
            [(1,2),(4,4)]
            ]
        ChangeTransform.changer(self,changes_6,tex6,tex6)
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
        for letter, color in [("(",RED), (")",RED)]:
            tex7.set_color_by_tex(letter,color)
            tex8.set_color_by_tex(letter,color)
        self.play(ApplyMethod(tex7.shift, LEFT*4.8+UP*0.5))
        tex8.next_to(tex7,RIGHT, buff = 0.1)
        tex9.next_to(tex8, RIGHT, buff = 0.1)
        self.wait()
        self.play(Write(tex8[0]))
        self.play(Write(tex8[2:4]))
        changes_7=[
            [(0,3),(1,4)]
            ]
        ChangeTransform.changer(self, changes_7,tex7,tex8)
        self.wait()
        self.play(Write(tex8[5]))
        self.play(Write(tex9[0]))
        changes_8=[
            [(2,3),(1,1)]
            ]
        ChangeTransform.changer(self,changes_8,tex8,tex9)
        self.wait()
        self.play(Write(tex9[2]))
        changes_9=[
            [(0,1),(3,3)]
            ]
        ChangeTransform.changer(self,changes_9,tex9,tex9)
        self.wait()
        #Transition to Distributivgesetz example
        self.play(FadeOut(tex7),run_time =0.1)
        self.play(FadeOut(tex8),run_time =0.1)
        self.play(FadeOut(tex9),run_time =0.1)
        text4.shift(1.5*UP+0.2*RIGHT)
        tex3.shift(1.5*UP+0.2*RIGHT)
        self.play(FadeOut(tex2),run_time=0.1)
        self.play(FadeOut(text3))
        self.play(FadeIn(text4))
        self.play(FadeIn(tex3), run_time=0.1)
        # Example Distributivgesetz
        for letter, color in [("\\cdot 6",RED)]:
            step1.set_color_by_tex(letter,color)
            step2.set_color_by_tex(letter,color)
        self.play(ApplyMethod(step1.shift, LEFT*4.8+UP*0.5))
        step2.next_to(step1,RIGHT, buff = 0.1)
        step3.next_to(step2, RIGHT, buff = 0.1)
        self.play(Write(step2[0]))
        self.play(Write(step2[2]))
        self.wait()
        changes_10 =[
            [(4,4),(1,3)]
            ]
        ChangeTransform.changer(self,changes_10,step1,step2)
        self.wait()
        self.play(Write(step2[4]))
        self.wait()
        changes_11=[
            [(0,1,2,3),(0,0,2,2)]
            ]
        self.play(Write(step3[1]))
        ChangeTransform.changer(self,changes_11,step2,step3)
        self.wait()
        self.play(Write(step3[3]))
        changes_12=[
            [(0,2),(4,4)]
            ]
        self.wait()
        ChangeTransform.changer(self,changes_12,step3,step3)
        self.wait(3) 

class Advantages5(Scene):
    def construct(self):
        #objects
        #helpers
        c = ChangeTransform()
        #texts
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
        tex4 = TexMobject("7", #0
                           "+ (-5)", #1
                           "+ 3", #2
                           "=",#3
                           )
        tex5 = TexMobject("7", #0
                           "+ 3", #1
                           "+ (-5)", #2
                           )
        tex6 = TexMobject("=",#0
                           "10", #1
                           "+ (-5)", #2
                           "=",#3
                           "5",#4
                            )
        tex7 = TexMobject("[", #0
                           "12 +", #1
                           "(-7)", #2
                           "]", #3
                           "+ (-3)", #4
                           "=", #5
                           )
        tex8 = TexMobject("12 +", #0
                           "[", #1
                           "(-7)", #2
                           "+ (-3)", #3
                           "]", #4
                           "=", #5
                           )
        tex9 = TexMobject("12 + ", #0
                           "(-10)", #1
                           "=", #2
                           "2", #3
                           )
        step1 = TexMobject("[",# 0
                           "13", #1
                           "+(-5)", #2
                           "]", #3
                           "\\cdot 3", #4
                           "=", #5
                           )
        step2 = TexMobject("13", #0
                           "\\cdot 3", #1
                           "+ (-5)", #2
                           "\\cdot 3",#3
                           "=", #4
                           )
        step3 = TexMobject("39", #0
                           "+", #1
                           "(-15)", #2
                           "=", #3
                           "24", #4
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
        ChangeTransform.changer(self,changes,tex1,tex1)   
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
        ChangeTransform.changer(self,changes_2,tex2,tex2)
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
        ChangeTransform.changer(self,changes_3,tex3,tex3)
        self.wait()
        self.play(ApplyMethod(tex3.next_to, text4, RIGHT))
        self.wait(2)
        self.play(FadeOut(text1))
        self.play(FadeOut(text3),run_time=0.1)
        self.play(FadeOut(text4), run_time=0.1)
        self.play(FadeOut(tex2), run_time=0.1)
        self.play(FadeOut(tex3), run_time=0.1)
        self.remove(text3,text4,tex2,tex3)
        self.wait(1)
        #Transistion
        self.play(GrowFromCenter(text5))
        self.play(ApplyMethod(text5.to_corner, UL))
        #Example Kommutativgesetz
        tex4[1].set_color(RED)
        tex4[2].set_color(BLUE)
        tex5[1].set_color(BLUE)
        tex5[2].set_color(RED)
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
        ChangeTransform.changer(self,changes_4,tex4,tex5)
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
        ChangeTransform.changer(self,changes_5,tex5,tex6)
        self.play(Write(tex6[3]))
        self.wait()
        changes_6=[
            [(1,2),(4,4)]
            ]
        ChangeTransform.changer(self,changes_6,tex6,tex6)
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
        for letter, color in [("(",RED), (")",RED)]:
            tex7.set_color_by_tex(letter,color)
            tex8.set_color_by_tex(letter,color)
        self.play(ApplyMethod(tex7.shift, LEFT*4+UP*0.5))
        tex8.next_to(tex7,RIGHT, buff = 0.1)
        tex9.next_to(tex8, RIGHT, buff = 0.1)
        self.wait()
        self.play(Write(tex8[0]))
        self.play(Write(tex8[2:4]))
        changes_7=[
            [(0,3),(1,4)]
            ]
        ChangeTransform.changer(self, changes_7,tex7,tex8)
        self.wait()
        self.play(Write(tex8[5]))
        self.play(Write(tex9[0]))
        changes_8=[
            [(2,3),(1,1)]
            ]
        ChangeTransform.changer(self,changes_8,tex8,tex9)
        self.wait()
        self.play(Write(tex9[2]))
        changes_9=[
            [(0,1),(3,3)]
            ]
        ChangeTransform.changer(self,changes_9,tex9,tex9)
        self.wait()
        #Transition to Distributivgesetz example
        self.play(FadeOut(tex7),run_time =0.1)
        self.play(FadeOut(tex8),run_time =0.1)
        self.play(FadeOut(tex9),run_time =0.1)
        text4.shift(1.5*UP+0.2*RIGHT)
        tex3.shift(1.5*UP+0.2*RIGHT)
        self.play(FadeOut(tex2),run_time=0.1)
        self.play(FadeOut(text3))
        self.play(FadeIn(text4))
        self.play(FadeIn(tex3), run_time=0.1)
        # Example Distributivgesetz
        for letter, color in [("\\cdot 3",RED)]:
            step1.set_color_by_tex(letter,color)
            step2.set_color_by_tex(letter,color)
        self.play(ApplyMethod(step1.shift, LEFT*4.8+UP*0.5))
        step2.next_to(step1,RIGHT, buff = 0.1)
        step3.next_to(step2, RIGHT, buff = 0.1)
        self.play(Write(step2[0]))
        self.play(Write(step2[2]))
        self.wait()
        changes_10 =[
            [(4,4),(1,3)]
            ]
        ChangeTransform.changer(self,changes_10,step1,step2)
        self.wait()
        self.play(Write(step2[4]))
        self.wait()
        changes_11=[
            [(0,1,2,3),(0,0,2,2)]
            ]
        self.play(Write(step3[1]))
        ChangeTransform.changer(self,changes_11,step2,step3)
        self.wait()
        self.play(Write(step3[3]))
        changes_12=[
            [(0,2),(4,4)]
            ]
        self.wait()
        ChangeTransform.changer(self,changes_12,step3,step3)
        self.wait(3) 
                