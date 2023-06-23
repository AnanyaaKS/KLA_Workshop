# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
f = open('input.json')
data = json.load(f)
#die info
width= data['die']['width']
print(width)
height= data['die']['height']
print(height)
rows =data['die']['rows']
print(rows)
columns= data['die']['columns']
print(columns)

#Streetwidth
stw = data ['street_width']
print(stw)

#Care_areas
catl= data['care_areas']
print(catl[0]['top_left'])
# The coordinates for x and y for top_left
x1= catl[0]['top_left']['x']
y1= catl[0]['top_left']['y']
print(x1)
print(y1)
cabr= data['care_areas']
print(cabr[0]['bottom_right'])
#the coordinates for x and y for bottom_right
x2= cabr[0]['bottom_right']['x']
y2= cabr[0]['bottom_right']['y']
print(x2)
print(y2)

# Closing file
f.close()

#Stitching the images 
imglist = ['Z:\KLA\wafer_image_1.png','Z:\KLA\wafer_image_2.png','Z:\KLA\wafer_image_3.png','Z:\KLA\wafer_image_4.png','Z:\KLA\wafer_image_5.png']
# Size of image
from  PIL import Image
for i in imglist:
    img = Image.open(i)
    width,height =img.size
    print(width)
    print(height)

    if (width != 800 or height != 600 ):
        print ('Image needs to be resized ')
        new_image = img.resize((800, 600))
        new_image.save('resized_image_wafer')
    
    else :
        print('Image same size')
    
for i in imglist:
    img= Image.open(i)
    #img.show()
    
d=0
l=0    
for i in imglist:
    img = Image.open(i)
    width,height= img.size
    d=d+width
    l=max(l,height)

print(d)
print(l)
result = Image.new('RGB', (d, l))
#result.show()

x=0
y=0
for i in imglist:
   j = Image.open(i)
   result.paste(j,box=(x,y))
   k,l = j.size
   x = x + k
   

result.save("merged_png","PNG")
#The stitched up  
#result.show()
    

#Error detedtion 
# Logic we need to take the images and 
#superimpose them and find the defects
'''
import numpy as np
from PIL import ImageChops
with Image.open ('Z:\KLA\wafer_image_1.png') as left:
    left.load()

with Image.open ('Z:\KLA\wafer_image_2.png') as right:
    right.load()

left_array = np.asarray(left)
right_array = np.asarray(right)
difference_array =  right_array - left_array
print(difference_array)
difference = Image.fromarray(difference_array)
difference.show()
diff_image = ImageChops.difference(left, right)
#coords = np.argwhere(difference_array > [0 0 0])
print(coords)

'''
from PIL import ImageChops
import csv

def find_differences(image1, image2, threshold=50):
    # Resize images
    image1 = image1.resize(image2.size)

    # Calculate the difference
    diff_image = ImageChops.difference(image1, image2)

    # Convert to grayscale
    diff_image = diff_image.convert('L')

    # Threshold the image
    diff_image = diff_image.point(lambda p: p > threshold and 255)

    # Find the differing coordinates
    differing_coordinates = []
    width, height = diff_image.size
    for y in range(height):
        for x in range(width):
            pixel = diff_image.getpixel((x, y))
            if pixel != 0:
                differing_coordinates.append((x, y))

    return differing_coordinates

# Load the images
image1 = Image.open('Z:\KLA\wafer_image_1.png')
image2 = Image.open('Z:\KLA\wafer_image_2.png')
image3 = Image.open('Z:\KLA\wafer_image_3.png')
image4 = Image.open('Z:\KLA\wafer_image_4.png')
image5 = Image.open('Z:\KLA\wafer_image_5.png')

# Find the differences
differences = find_differences(image1, image2)
differences2 = find_differences(image3, image4)
differences3 = find_differences(image5, image1)
differences4 = find_differences(image4, image2)
differences5 = find_differences(image2, image3)
differences6 = find_differences(image1, image3)
differences7 = find_differences(image1, image4)
differences8 = find_differences(image2, image5)
differences9 = find_differences(image3, image1)
differences10 = find_differences(image3, image5)



defect_points=[]
# Print the differing coordinates
for coord in differences  and  differences6 and differences7:
    print(coord)
    defect_points.append((1,coord[0],coord[1]))
    
for coord in differences5 and differences8:
    print(coord)
    defect_points.append((2,coord[0],coord[1]))
    
for coord in differences2 and differences9 and differences10:
    print(coord)
    defect_points.append((3,coord[0],coord[1]))

for coord in differences4:
    print(coord)
    defect_points.append((4,coord[0],coord[1]))
    
for coord in differences3:
    print(coord)
    defect_points.append((5,coord[0],coord[1]))
    
with open("output10.csv","a+") as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerows(defect_points)