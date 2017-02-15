#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

def setColorMap(name:str="default"):
    colormap=[1,1,1]*16
    if name=="rainbow":        
        colormap[ 0]=[255,   0,   0]
        colormap[ 1]=[255,  80,   0]
        colormap[ 2]=[255, 180,   0]
        colormap[ 3]=[255, 255,   0]
        colormap[ 4]=[192, 255,   0] 
        colormap[ 5]=[128, 255,   0] 
        colormap[ 6]=[ 64, 255,   0] 
        colormap[ 7]=[  0, 255,   0] 
        colormap[ 8]=[  0, 192,  64] 
        colormap[ 9]=[  0, 128, 128] 
        colormap[10]=[  0,  64, 192] 
        colormap[11]=[  0,   0, 255] 
        colormap[12]=[ 64,   0, 255] 
        colormap[13]=[128,   0, 255] 
        colormap[14]=[192,   0, 255] 
        colormap[15]=[255,   0, 255] 
    elif name=="forest":        
        colormap[ 0]=[142,  94,   5] # d.braun
        colormap[ 1]=[180, 120,   7]
        colormap[ 2]=[210, 150,  12]
        colormap[ 3]=[240, 165,  32] # h.braun
        colormap[ 4]=[180, 165,  14] 
        colormap[ 5]=[150, 130,  10] 
        colormap[ 6]=[100,  80,   7] 
        colormap[ 7]=[ 50,  60,   4] 
        colormap[ 8]=[  0,  42,   0] # d.grün 
        colormap[ 9]=[ 20,  92,  20] 
        colormap[10]=[ 40, 142,  40] 
        colormap[11]=[ 60, 192,  60] 
        colormap[12]=[ 80, 225,  80] 
        colormap[13]=[ 96, 255,  96] # h.grün
        colormap[14]=[132, 180,  45] 
        colormap[15]=[160, 105,   6] 
    elif name=="planet":        
        colormap[ 0]=[255, 255, 255] # weiß
        colormap[ 1]=[227, 227, 255]
        colormap[ 2]=[200, 200, 255] # h.blau
        colormap[ 3]=[150, 150, 200]
        colormap[ 4]=[100, 100, 120] 
        colormap[ 5]=[ 50,  50,  80] 
        colormap[ 6]=[  0,   0,  42] # d.blau 
        colormap[ 7]=[  2,  16,  32] 
        colormap[ 8]=[  4,  32,  24] 
        colormap[ 9]=[  7,  48,  16] 
        colormap[10]=[ 10,  64,  10] # d.gn 
        colormap[11]=[ 80, 150,  85] 
        colormap[12]=[170, 255, 180] # h.gn
        colormap[13]=[130, 200, 120] 
        colormap[14]=[ 90, 120,  60] 
        colormap[15]=[ 42,  42,   0] # d.bn
    elif name=="fire":        
        colormap[ 0]=[  0,   0,   0] # bk
        colormap[ 1]=[ 32,  32,   5]
        colormap[ 2]=[ 64,  32,   8] # d.red
        colormap[ 3]=[128,  64,   8]
        colormap[ 4]=[192,   0,   0] 
        colormap[ 5]=[210,   0,   0] 
        colormap[ 6]=[255,   0,   0] 
        colormap[ 7]=[255,  30,  30] #red! 
        colormap[ 8]=[255,  60,  23] 
        colormap[ 9]=[255, 120,  14] 
        colormap[10]=[255, 200,   7] 
        colormap[11]=[255, 255, 0] 
        colormap[12]=[250, 250, 0] 
        colormap[13]=[245, 245, 0] 
        colormap[14]=[240, 240, 255] 
        colormap[15]=[255, 255, 255]
    else:  
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
    return colormap
  
"""
    elif name=="":        
        colormap[ 0]=[]
        colormap[ 1]=[]
        colormap[ 2]=[]
        colormap[ 3]=[]
        colormap[ 4]=[] 
        colormap[ 5]=[] 
        colormap[ 6]=[] 
        colormap[ 7]=[] 
        colormap[ 8]=[] 
        colormap[ 9]=[] 
        colormap[10]=[] 
        colormap[11]=[] 
        colormap[12]=[] 
        colormap[13]=[] 
        colormap[14]=[] 
        colormap[15]=[]
"""