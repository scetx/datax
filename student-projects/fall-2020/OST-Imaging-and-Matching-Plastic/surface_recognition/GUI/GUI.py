import tkinter as tk
from PIL import ImageTk, Image
from os import listdir
import cv2
import numpy as np


root=tk.Tk()
root.title("DataX: Team OST, Plastic Part Matching")

#Init database
path=r"C:\Users\tobias.grab\IWK_data\test"
files=listdir(path)
nrOfFiles=len(files)

bf = cv2.BFMatcher()
fast=1
if fast==1:
    img_database=np.load(r"C:\Users\tobias.grab\IWK_data\savedArrays\img_database.npy")
    img_database=[img_database[i,:,:] for i in range(len(files))]
else:
    img_database=[cv2.imread(path+'\\'+file,0) for file in files]
img_database_pillow=[ImageTk.PhotoImage(Image.fromarray(img).resize((320, 240),Image.ANTIALIAS)) for img in img_database]


def open_file():
    from tkinter.filedialog import askopenfilename
    file_path = askopenfilename(title=u'select file')
    name=file_path.split("/")[-1]
    img_to_match=cv2.imread(file_path,0)
    img_to_match_pillow=ImageTk.PhotoImage(Image.fromarray(img_to_match).resize((320, 240),Image.ANTIALIAS))
    
    if v.get()==1:
        ALG=cv2.xfeatures2d.SURF_create()
    elif v.get()==2:
        ALG=cv2.xfeatures2d.SURF_create()
    elif v.get()==3:
        ALG=cv2.BRISK_create()
    elif v.get()==4:
        ALG=cv2.AKAZE_create()
    elif v.get()==5:
        ALG=cv2.KAZE_create()
    img_database_fts=[ALG.detectAndCompute(img, None) for img in img_database]
    draw_database=[ImageTk.PhotoImage(Image.fromarray(
        cv2.drawKeypoints(img_from_database, img_database_fts[nr][0],None)).resize((320, 240),Image.ANTIALIAS)
        ) for nr, img_from_database in enumerate(img_database)]

    
    
    (kps1, descs1) = ALG.detectAndCompute(img_to_match, None)
    
    layout2=tk.Label(root)
    layout2.place(relx=0.5,rely=0, relwidth=1, relheight=1,anchor='n')
    
    label_img_to_match=tk.Label(layout2,image=img_to_match_pillow)
    label_img_to_match.image=img_to_match_pillow
    label_img_to_match.place(relx=0.3,rely=0.1, width=320, height=240,anchor='n')

    label_img_database=tk.Label(layout2,image=draw_database[0])
    label_img_database.image=draw_database[0]
    label_img_database.place(relx=0.7,rely=0.1, width=320, height=240,anchor='n')

    label_img_matched=tk.Label(layout2,image=draw_database[0])
    label_img_matched.image=draw_database[0]
    label_img_matched.place(relx=0.5,rely=0.5, width=640, height=240,anchor='n')
    
    nrOfGoodPerImage=np.zeros([nrOfFiles,1])
    
    image_list_matched=[]    
    
    def calc(j):
        if j<nrOfFiles-1:
            bf = cv2.BFMatcher()
            kps2=img_database_fts[j][0]
            descs2=img_database_fts[j][1]
            matches = bf.knnMatch(descs1,descs2,k=2)
            matchesMask = [[0,0] for i in range(len(matches))]
                
            for i,(m,n) in enumerate(matches):
                if m.distance < 0.75*n.distance:
                    matchesMask[i]=[1,0]
            good = []
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    good.append([m])
                    
            
            nrOfGoodPerImage[j]=np.sum(matchesMask[:])
            
            img3 = cv2.drawMatchesKnn(img_to_match,kps1,img_database[j],kps2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            img3_pillow=ImageTk.PhotoImage(Image.fromarray(img3).resize((640, 240),Image.ANTIALIAS))
            image_list_matched.append(img3_pillow)
            root.after(0, calc(j+1))
    
    calc(0)
    idx = (-np.squeeze(nrOfGoodPerImage)).argsort()[:3]

    
    def matching(i):
        if i<nrOfFiles-1:
            
            label_img_database.config(image=draw_database[i])
            label_img_matched.config(image=image_list_matched[i])
            root.after(DELAY, lambda: matching(i+1))
        elif i==nrOfFiles-1:
            # my_label4=tk.Label(root,bg='#80c1ff')
            my_label4=tk.Label(root,bg="LightSteelBlue1")
            my_label4.place(relx=0.5,rely=0, relwidth=1, relheight=1,anchor='n')
            
            org_label=tk.Label(my_label4,text="Image to match:\n"+name)
            org_label.place(relx=0.15,rely=0.5,anchor='e')
            org=tk.Label(my_label4,image=img_to_match_pillow)
            org.place(relx=0.15,rely=0.5, width=320, height=240,anchor='w')
            
            best_match_label=tk.Label(my_label4,text="Best Match:\n"+files[idx[0]])
            best_match_label.place(relx=0.8,rely=0.2,anchor='w')
            best_match=tk.Label(my_label4,image=img_database_pillow[idx[0]])
            best_match.place(relx=0.8,rely=0.2, width=320, height=240,anchor='e')
            
            best_match2_label=tk.Label(my_label4,text="Second Best Match:\n"+files[idx[1]])
            best_match2_label.place(relx=0.8,rely=0.5,anchor='w')
            best_match2=tk.Label(my_label4,image=img_database_pillow[idx[1]])
            best_match2.place(relx=0.8,rely=0.5, width=320, height=240,anchor='e')
            
            best_match3_label=tk.Label(my_label4,text="Third Best Match:\n"+files[idx[2]])
            best_match3_label.place(relx=0.8,rely=0.8,anchor='w')
            best_match3=tk.Label(my_label4,image=img_database_pillow[idx[2]])
            best_match3.place(relx=0.8,rely=0.8, width=320, height=240,anchor='e')
            
            # my_title2=tk.Label(my_label4,text="Matching finished! Displaying results...",font=("Helvetica",20), bg='#80c1ff')
            my_title2=tk.Label(my_label4,text="Matching finished! Displaying results...",font=("Helvetica",20), bg="LightSteelBlue1")
            my_title2.place(relx=0.5,rely=0.0, relwidth=0.4, relheight=0.05,anchor='n')
    
    matching(0)
        
DELAY=10
HEIGHT=900
WIDTH=1400

canvas=tk.Canvas(root,height=HEIGHT, width=WIDTH)
canvas.pack()

# button_quit= tk.Button(root, text="Exit Program", command=root.quit)
# button_quit.pack()

my_title=tk.Label(root,text="Choose the algorithm you want to use",font=("Helvetica",16))
my_title.place(relx=0.5,rely=0.0, relwidth=0.4, relheight=0.1,anchor='n')

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("SIFT",1),
    ("SURF",2),
    ("BRISK",3),
    ("AKAZE",4),
    ("KAZE",5)
    ]

for txt, val in languages:
    tk.Radiobutton(root, 
                text=txt,
                padx = 10, pady=10,
                variable=v, 
                value=val).place(relx=0.5,rely=0.1+val/40, relwidth=0.1, relheight=0.025,anchor='n')

my_title1=tk.Label(root,text="Choose the testimage:",font=("Helvetica",16))
my_title1.place(relx=0.5,rely=0.525, relwidth=0.4, relheight=0.1,anchor='n')

btn = tk.Button(root, text ='Open', command = lambda: open_file(),bg="LightSteelBlue1") 
btn.place(relx=0.5,rely=0.6, relwidth=0.6, relheight=0.2,anchor='n')





root.mainloop()