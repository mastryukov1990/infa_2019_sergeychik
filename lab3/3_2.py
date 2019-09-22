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
rectangle(0, 0, 1000, 300)
brushColor(0,128,85)
rectangle(0,300, 1000, 800)
penColor(233,99,233)
brushColor(233,99,233)
polygon([(350,210),(425,400),(275,400),(350,210)])
polygon([(1000-350,210),(1000-425,400),(1000-275,400),(1000-350,210)])
penColor(133,133,133)
brushColor(133,133,133)
ellipse( 50, 95, 150, 305)
ellipse( 50, 95,1000- 150, 305)
penColor(255,255,255)
brushColor(255,255,255)
circle(150,180,50)
circle(350,180,50)
circle(1000-150,180,50)
circle(1000-350,180,50)
penSize(1)
penColor(0,0,0)
line(375, 400, 375, 500)
line(1000-375, 400,1000-375, 500)
line(375, 500, 390, 505)
line(1000-375, 500,1000- 390, 505)
line(325, 400, 325, 500)
line(1000-325, 400,1000- 325, 500)
line(325, 500, 310, 500)
line(1000-325, 500,1000- 310, 500)
line(360,240,425,320)
line(1000-360,240,1000-425,320)
line(425,320,500,260)
line(1000-425,320,1000-500,260)
line(340,240,275,320)
line(1000-340,240,1000-275,320)
line(276,321,180,250)
line(1000-276,321,1000-180,250)
line(110,250,70,360)
line(68,371,55,215)
penColor(255,0,0)
brushColor(255,0,0)
polygon([(55,215),(35,150),(70,145),(55,215)])
circle(45,150,10)
circle(60,147,10)
line(1000-110,250,1000-70,360)
line(160,390,190,500)
line(1000-160,390,1000-190,500)
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