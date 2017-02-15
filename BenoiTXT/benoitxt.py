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
        self.maxiter=32
        

        
        # create the empty main window
        self.w = TouchWindow("BenoiTxt")
        
      
        # create central widget
        
        self.centralwidget=QWidget()
        
        self.layout=QVBoxLayout()
        self.layout.addStretch()
        
        self.text=QLabel()
        self.text.setText("...yawn...")
        self.text.setObjectName("smalllabel")
        self.text.setAlignment(Qt.AlignCenter)
        
        self.layout.addWidget(self.text)
        self.layout.addStretch()
        
        self.progress=QProgressBar()
        self.progress.setMaximum(100)
        self.progress.setMinimum(0)
        self.progress.setValue(0)
        
        self.layout.addWidget(self.progress)
        self.layout.addStretch()
        
        self.knopf=QPushButton("Start")
        self.knopf.clicked.connect(self.rechne)
        
        self.layout.addWidget(self.knopf)
        
        self.centralwidget.setLayout(self.layout)
        
        self.w.setCentralWidget(self.centralwidget)
        
        self.w.show()

        # create an overlay pixmap:
  
        self.bild = QLabel(self.w)
        self.bild.setGeometry(0, 0, 240, 320)
        self.bild.setPixmap(QPixmap(240,320))

        self.bild.mousePressEvent=self.on_bild_clicked
        
        self.timer=QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.on_timer)
        self.exec_()
         
    def on_timer(self):
        #self.processEvents()
        pass
    
    def void(self,event):
        print("void:",event)
    
    def on_bild_clicked(self,sender):
        print(sender.type)
        if self.bild.isVisible:  self.bild.hide()
        else: self.bild.show()
        
    def rechne(self):
        print("sr")
        self.timer.start()
        self.text.setText("...computing")
        self.progress.setValue(0)
        (xv,yv,m)=mandelbrot_set2(self.xmin, self.xmax, self.ymin, self.ymax, 320, 240, self.maxiter, self.progress)
        self.mand2pixmap(320,240,m,self.maxiter,self.bild.pixmap())
        
        self.text.setText("...ready")
        self.timer.stop()
        self.bild.show()
        
        
    def colorize(self, n, maxiter):
        if n>0 and n<maxiter:
          return colormap[int(n % 16)]
        else:
          return 0,0,0

    def mand2pixmap(self,width,height,mand, maxiter, pixmap):
       
        p = QPainter()
        p.begin(pixmap)
        for i in range(width):
            
            for j in range(height):
                (r,g,b)=self.colorize(mand[i,j],maxiter)

                p.setPen(QColor(r,g,b,255))
                p.drawPoint(QPoint(height-j-1,width-i-1))
        p.end()
          
def mandelbrot_set2(xmin,xmax,ymin,ymax,width,height,maxiter, progress):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    nup=100/(width*height)
    z=0
    for i in range(width):
        for j in range(height):
            n3[i,j]=mandelbrot(r1[i],r2[j],maxiter)
            z=z+1
            progress.setValue(z*nup)
          
    return r1,r2,n3

def mandelbrot(creal,cimag,maxiter):
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
  
if __name__ == "__main__":
    FtcGuiApplication(sys.argv)
