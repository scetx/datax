# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:59:38 2020

@author: tobias.grab
"""


import tkinter as tk
from PIL import ImageTk, Image
from os import listdir
import cv2
import numpy as np

root=tk.Tk()
root.title("DataX: Team OST, Plastic Part Matching")

def clock(i):
    my_label.config(image=image_list[i])
    my_label2.config(image=image_list_matched[i])
    
    if i<nrOfFiles-1:
        i=i+1
        my_label.after(DELAY,lambda: clock(i))
        
    else:
        my_label4=tk.Label(root,bg='#80c1ff')
        my_label4.place(relx=0.5,rely=0, relwidth=1, relheight=1,anchor='n')
        
        org_label=tk.Label(my_label4,text="Image to match:\n"+name)
        org_label.place(relx=0.15,rely=0.5,anchor='e')
        org=tk.Label(my_label4,image=img_to_match_pillow)
        org.place(relx=0.15,rely=0.5, width=320, height=240,anchor='w')
        
        best_match_label=tk.Label(my_label4,text="Best Match:\n"+files[idx[0]])
        best_match_label.place(relx=0.8,rely=0.2,anchor='w')
        best_match=tk.Label(my_label4,image=image_list[idx[0]])
        best_match.place(relx=0.8,rely=0.2, width=320, height=240,anchor='e')
        
        best_match2_label=tk.Label(my_label4,text="Second Best Match:\n"+files[idx[1]])
        best_match2_label.place(relx=0.8,rely=0.5,anchor='w')
        best_match2=tk.Label(my_label4,image=image_list[idx[1]])
        best_match2.place(relx=0.8,rely=0.5, width=320, height=240,anchor='e')
        
        best_match3_label=tk.Label(my_label4,text="Third Best Match:\n"+files[idx[2]])
        best_match3_label.place(relx=0.8,rely=0.8,anchor='w')
        best_match3=tk.Label(my_label4,image=image_list[idx[2]])
        best_match3.place(relx=0.8,rely=0.8, width=320, height=240,anchor='e')
        
        my_title2=tk.Label(my_label4,text="Matching finished! Displaying results...",font=("Helvetica",20), bg='#80c1ff')
        my_title2.place(relx=0.5,rely=0.0, relwidth=0.4, relheight=0.05,anchor='n')

name="org_Nr381.jpg"
path=r"C:\Users\tobias.grab\IWK_data\test"
matcher="bf" #bf or flann

files=listdir(path)
nrOfFiles=len(files)
image_list=[ImageTk.PhotoImage(Image.open(path+"\\"+files[nr]).resize((320, 240),Image.ANTIALIAS)) for nr in range(nrOfFiles)]
# SURF=cv2.xfeatures2d.SURF_create()
SURF=cv2.BRISK_create()
img_to_match=cv2.imread(path+"\\"+name,0)

(kps1, descs1) = SURF.detectAndCompute(img_to_match, None)

nrOfGoodPerImage=np.zeros([nrOfFiles,1])
DistPerImage=np.zeros([nrOfFiles,1])
bauteilnr=0
img1 = cv2.drawKeypoints(img_to_match, kps1, None)



image_list_matched=[]
for file in files:
    img_from_database = cv2.imread(path+'\\'+file,0)    
    (kps2, descs2) = SURF.detectAndCompute(img_from_database, None)
    img2 = cv2.drawKeypoints(img_from_database, kps2, None)
    
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(descs1,descs2,k=2)
    matchesMask = [[0,0] for i in range(len(matches))]
        
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.75*n.distance:
            matchesMask[i]=[1,0]
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
            
    
    nrOfGoodPerImage[bauteilnr]=np.sum(matchesMask[:])
    bauteilnr=bauteilnr+1
    # img3 = cv2.drawMatchesKnn(img1,kps1,img2,kps2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)
    
    img3 = cv2.drawMatchesKnn(img_to_match,kps1,img_from_database,kps2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    img3_pillow=ImageTk.PhotoImage(Image.fromarray(img3).resize((640, 240),Image.ANTIALIAS))
    image_list_matched.append(img3_pillow)


idx = (-np.squeeze(nrOfGoodPerImage)).argsort()[:3]




DELAY=10
HEIGHT=900
WIDTH=1400 

canvas=tk.Canvas(root,height=HEIGHT, width=WIDTH)
canvas.pack()


img_to_match_pillow=ImageTk.PhotoImage(Image.fromarray(img_to_match).resize((320, 240),Image.ANTIALIAS))

my_label=tk.Label(root,image=image_list[0])
my_label.place(relx=0.7,rely=0.1, width=320, height=240,anchor='n')

my_label2=tk.Label(root,image=image_list[1])
my_label2.place(relx=0.5,rely=0.5, width=640, height=240,anchor='n')

my_label3=tk.Label(root,image=img_to_match_pillow)
my_label3.place(relx=0.3,rely=0.1, width=320, height=240,anchor='n')

my_title=tk.Label(root,text="Matching in progress...",font=("Helvetica",20))
my_title.place(relx=0.5,rely=0.0, relwidth=0.3, relheight=0.1,anchor='n')

button_quit= tk.Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


clock(0)

root.mainloop()
