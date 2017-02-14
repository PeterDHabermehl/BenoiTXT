#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

import numpy as np
import sys
from TouchStyle import *

colormap=[1,1,1]*16
colormap[ 0]=[ 66,  30,  15]
colormap[ 1]=[ 25,   7,  26]
colormap[ 2]=[  9,   1,  47]
colormap[ 3]=[  4,   4,  73]
colormap[ 4]=[  0,   7, 100] # blue 4
colormap[ 5]=[ 12,  44, 138] # blue 3
colormap[ 6]=[ 24,  82, 177] # blue 2
colormap[ 7]=[ 57, 125, 209] # blue 1
colormap[ 8]=[134, 181, 229] # blue 0
colormap[ 9]=[211, 236, 248] # lightest blue
colormap[10]=[241, 233, 191] # lightest yellow
colormap[11]=[248, 201,  95] # light yellow
colormap[12]=[255, 170,   0] # dirty yellow
colormap[13]=[204, 128,   0] # brown 0
colormap[14]=[153,  87,   0] # brown 1
colormap[15]=[106,  52,   3] # brown 2

abort=False

class FtcGuiApplication(TouchApplication):
    def __init__(self, args):
        TouchApplication.__init__(self, args)

        translator = QTranslator()
        path = os.path.dirname(os.path.realpath(__file__))
        translator.load(QLocale.system(), os.path.join(path, "benoitxt_"))
        self.installTranslator(translator)

        self.xmin=-2.4
        self.xmax=0.9
        self.ymin=-1.25
        self.ymax=1.25
        self.maxiter=24
               
        # create the empty main window
        self.w = TouchWindow("BenoiTXT")
        
        # create an overlay pixmap:
  
        self.bild = QLabel(self.w)
        self.bild.setGeometry(0, 0, 240, 320)
        self.bild.setPixmap(QPixmap(240,320))
        
        self.invisible = QLabel(self.w)
        self.invisible.setGeometry(0,0,240,320)
        
        
        self.w.show()
        self.invisible.mousePressEvent=self.void
        QTimer.singleShot(800,self.rechne)
        self.exec_()
   
    def void(self,event):
        print("void:",event)
    
    def rechne(self,origin=None):
        self.invisible.hide()
        self.invisible.setDisabled(True)
        self.invisible.stackUnder(self.bild)
        self.mandelbrot_set2(self.xmin, self.xmax, self.ymin, self.ymax, 320, 240, self.maxiter, self.bild)
        self.invisible.show()
        self.invisible.setDisabled(False)
        self.bild.stackUnder(self.invisible)
        
    def colorize(self, n, maxiter):
        if n>0 and n<maxiter:
          return colormap[int(n % 16)]
        else:
          return 0,0,0

    def mandelbrot(self, creal,cimag,maxiter):
        real = creal
        imag = cimag
        for n in range(maxiter):
            real2 = real*real
            imag2 = imag*imag
            if real2 + imag2 > 4.0:
                return n
            imag = 2* real*imag + cimag
            real = real2 - imag2 + creal       
        return 0

    def mandelbrot_set2(self,xmin,xmax,ymin,ymax,width,height,maxiter,wi):
        r1 = np.linspace(xmin, xmax, width)
        r2 = np.linspace(ymin, ymax, height)
        n3 = np.empty((width,height))
        print("start")
        pm=wi.pixmap()

        for i in range(width):
            p = QPainter()
            p.begin(pm)
            for j in range(height):
                (r,g,b)=self.colorize(self.mandelbrot(r1[i],r2[j],maxiter),maxiter)

                p.setPen(QColor(r,g,b,255))
                p.drawPoint(QPoint(239-j,319-i))
            p.end()
            wi.repaint()

              
        print("stop")
        return
  
if __name__ == "__main__":
    FtcGuiApplication(sys.argv)