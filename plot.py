'''
Author: Diego Arenas
Date: 4/24/2022
Purpose: Script will count all class/index id from .txt file that is for YOLO dataset
and graph them from greates to least used.
'''


import time
start1 = time.time()
print("[->] Loading libraries...")

import os
import csv
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from typing import Counter
from operator import itemgetter

end1 = time.time()
print("[->] Python loaded libraries in {:.3} seconds.".format(end1-start1))

classTotal = 0
fileExt = '.txt'
imageFiles= []
ALLOWED_EXTENSIONS = ('.jpg', '.png', '.jpeg', '.JPG', '.PNG', '.JPEG')
boarder = "+------------------------------------------------------------------------------+"


DirPath =input("{}\n[->] Enter text files directory below\n->".format(boarder)) # User inputs directory to work on
start2 = time.time()
print(boarder)
print("[Processing] changing directory...")
print(boarder)
os.chdir(DirPath)  # Changes directory that user specified
#print ("[INFO] Current working on directory: %s" % os.getcwd()) # Outputs Current directory
#print("boarder")

classesFile = ("classes.txt")# defining classes.txt file. Stores labels of object detector
classes = open(classesFile)# Opens up classses.txt file
line = classes.read()# Reads data from classes.txt as string
classData = line.split("\n")
ids = len(classData)
classes.close()# closes classes.txt file

textFiles = [f for f in os.listdir(DirPath) if f.endswith('.txt')] #opens all files the end with .txt
textFiles.pop(textFiles.index("classes.txt"))

'''
for f in tqdm(textFiles, desc= "Retriving Files",ncols=80):
    with open(f,"r") as fileobj: #opens textFiles
        for data in fileobj: 
            imageFiles.append(f)
            #print(f,"/ " +data) # prints all the .txt files and data
'''
#counts total number of txt files
fileCounter = 0
for cnt in os.listdir(DirPath):
    if cnt.endswith('.txt'):
        fileCounter +=1

#counts total number of txt files
fileCounter = 0
for cnt in os.listdir(DirPath):
    if cnt.endswith('.txt'):
        fileCounter +=1

#counts total number of line in classes.txt
for i in classData:
    if i:
        classTotal +=1
print("[->] Total classes in dataset: {:,} \n".format(classTotal))

for i in range(ids):
    if( i % 10)-9:
        print(i,end=" ")
    else:
        print(i)
    
print("\n{}\n[->] {:,} Total # of .txt files detected\n{}".format(boarder, fileCounter, boarder))

textFiles.append("classes.txt")
c = 0
elids =[]
ids = []
IdDict ={}
start3 = time.time()

for f in tqdm(textFiles, desc= "Processing List Data",ncols=80):
    with open(f,"r") as fileobj: #opens textFiles
            with open(os.path.join(DirPath,f), "r") as newfileobj:
                    lines = fileobj.readlines()
                    for line in lines:
                        if (f != "classes.txt"):
                            oldLine = line.split() #turns the line into a list separated by white spaces to fix the case where the first number was a double digit
                            ClassId = oldLine[0] #grabs the old value so we can replace it
                            ids = [ClassId]
                            elids.extend(ids)
                            c+=1

end3 = time.time()
t = []
ecc =[]
ecc.extend(classData)

t = elids
t.sort(key=int)
t = Counter(elids).items()

header = ["Class Name","Class ID", "Count"]
la = [x for x,y in t]
lb = [y for x,y in t]
#print(t)

columns = {}
columns["Class Name"] = ecc
columns["Class IDs"] = la 
columns["Counts"] = lb
#rows  = zip(columns["Class IDs"],columns["Counts"] )
rows  = zip(columns["Class Name"],columns["Class IDs"],columns["Counts"] )

while True:
    try:
        csvFIle = open('Class_ID_Stats.csv', 'w')
        break
    except IOError:
        input("Could not open file! Please close Class_ID_Stats.csv. Press Enter to retry.")

with open('Class_ID_Stats.csv', 'w', newline='') as a:
    writers = csv.writer(a)
    writers.writerow(header)
    writers.writerows(rows)

elids.sort(key=itemgetter(0))
print("\n[->] Sorting though list took {0:.3} seconds".format(end3-start3))
print("[->] {:,} Class ID's counted".format(c))
end2 = time.time()
print("[->] Program took {0:.3} seconds to execute".format(end2-start2))

ClassIn, ax = zip(*t)
indexes = np.arange(len(ClassIn))
width =.7

for i in range(len(t)):
    plt.text(i, ax[i], ax[i],color='black',ha="center")
    
plt.title("Count of Class IDs in Dataset")
plt.bar(indexes, ax, width, color='green',edgecolor = 'black')
plt.grid(color='#95a5a6', linestyle='-', linewidth=.7, axis='y', alpha=0.7)
plt.xticks(indexes, ClassIn)

plt.show()


print("""+------------------------------------------------------------------------------+
+------------------------------------------------------------------------------+
|                               TASK COMPLETE                                  |  
+------------------------------------------------------------------------------+""")
