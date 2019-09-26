from graph import *
windowSize(1000,600)
canvasSize(1000,600)
from graph import *
def ellipse( a, b, x0, y0):
    x = a
    y = 0
    s = [(x0 + a, y0)]
    for i in range(2 * a):
        x -= 1
        y = ((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5
        s.append((x + x0, y + y0))
    for i in range(2 * a):
        x += 1
        y = -(((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5)
        s.append((x + x0, y + y0))
    polygon(s)
    
brushColor(80,230,230)
rectangle(0, 0, 1000, 300) #sky_view 
brushColor(0,128,85)
rectangle(0,300, 1000, 800)#land_view
penColor(233,99,233)
brushColor(233,99,233)
polygon([(850,210),(925,400),(775,400),(850,210)])#woman_body
polygon([(1000-850,210),(1000-925,400),(1000-775,400),(1000-850,210)])#woman_body
penColor(133,133,133)
brushColor(133,133,133)
ellipse( 50, 95, 350, 305)#man_body
ellipse( 50, 95,1000- 350,305)#man_body
penColor(255,255,255)
brushColor(255,255,255)
circle(150,180,50)#head
circle(350,180,50)#head
circle(1000-150,180,50)#head
circle(1000-350,180,50)#head
penSize(1)
penColor(0,0,0)

line(360, 400, 375, 500)
line(1000-360, 397,1000-375, 500)
line(375, 500, 390, 500)
line(1000-385, 500,1000- 375, 500)
line(340, 400, 325, 500)#men_legs
line(1000-340, 397,1000- 325, 500)
line(325, 500, 310, 500)
line(1000-324, 500,1000- 310, 500)
line(385,240,425,320)
line(1000-385,240,1000-425,320)
line(425,320,500,260)
line(1000-425,320,1000-500,250)
line(315,240,275,320)
line(1000-315,240,1000-275,320)
line(276,321,167,250)
line(1000-276,321,1000-167,250)
line(135,250,70,360)
line(70,366,55,215)
penColor(0,0,0)
brushColor(255,0,0)
polygon([(55,215),(35,150),(70,145),(55,215)])
circle(45,150,10)
circle(60,147,10)
line(1000-135,250,1000-70,360)
line(160,390,190,500)
line(1000-180,390,1000-190,500)
line(190,500,220,500)
line(1000-190,500,1000-220,500)
line(140,390,110,500)
line(1000-140,390,1000-110,500)
line(110,500,85,505)
line(1000-110,500,1000-85,505)
penColor(255,215,0)
brushColor(255,215,0)
polygon([(1000-77,370),(1000-57,270),(1000-19,305),(1000-77,370)])
penColor(139,69,19)
brushColor(139,69,19)
ellipse(14,10,1000-30,302)
penColor(255,0,0)
brushColor(255,0,0)
ellipse(14,12,1000-47,278)
penColor(255,255,255)
brushColor(255,255,255)
ellipse(15,12,1000-28,282)
penColor(0,0,0)
line(500,260,520,100)
penColor(255,215,0)
brushColor(255,215,0)
polygon([(520,100),(480,32),(560,32),(520,100)])
penColor(139,69,19)
brushColor(139,69,19)
ellipse(15,12,495,35)
penColor(255,0,0)
brushColor(255,0,0)
ellipse(15,12,545,35)
penColor(255,255,255)
brushColor(255,255,255)
ellipse(15,12,520,25)
run()
