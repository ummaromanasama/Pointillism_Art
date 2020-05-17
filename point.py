#Importing Libraries
from PIL import Image  
import numpy as np  
import matplotlib.pyplot as plt  
import cv2
import matplotlib.colors as colors

#Read image
myImage = cv2.imread('wreck.jpg')

#Display image
cv2.imshow('Wreck-It Ralph', myImage)

#Close window by pressing any key
cv2.waitKey(0)

#Number of dots
dot_number = 10

#Load image and convert to black and white
original_image = Image.open("wreck.jpg") 
bw_image = original_image.convert('1') 
bw_image_array = np.array(bw_image, dtype=np.int)  
black_indices = np.argwhere(bw_image_array == 0)  
chosen_black_indices = black_indices[np.random.choice(black_indices.shape[0], replace=False, size=dot_number)]  

#Generate dots with X and Y values
x = [x[1] for x in chosen_black_indices]
y = [x[0] for x in chosen_black_indices]

#Pair and store coordinates points
coordinates_values = zip(x,y)
image_coordinates = list(coordinates_values)

# IndexError: index 1137 is out of bounds for axis 0 with size 670
my_point=17, 47

coordinate_original = myImage[my_point]
print('Original GBR: ', coordinate_original)

bgr_to_rgb = cv2.cvtColor(myImage, cv2.COLOR_BGR2RGB)
coordinate_color = bgr_to_rgb[my_point]
print('New RGB: ', coordinate_color)

#How to convert RBG on 255 scale to 0-1
conversion_forumla = coordinate_color/255
print('0-1 scale:', conversion_forumla)

rgb_to_hex = colors.rgb2hex(conversion_forumla)
print('Hexdecimal', rgb_to_hex)

#IndexError: index 1027 is out of bounds for axis 0 with size 670
for i in image_coordinates:
    print(myImage[i])

#Change dot color here
plt.plot(x, y, 'o', color= rgb_to_hex)
plt.show()
