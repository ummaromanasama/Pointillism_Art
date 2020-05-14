from PIL import Image  
import numpy as np  
import matplotlib.pyplot as plt  

#Load image and convert to black and white
original_image = Image.open("jg.jpg") 
bw_image = original_image.convert('1') 
bw_image_array = np.array(bw_image, dtype=np.int)  
black_indices = np.argwhere(bw_image_array == 0)  
chosen_black_indices = black_indices[np.random.choice(black_indices.shape[0], replace=False, size=100000)]  

#Generate dots with X and Y values
x = [x[1] for x in chosen_black_indices]
y = [x[0] for x in chosen_black_indices]

#Code I think I might need
# #Change mask 
# change_mask = 'https://logos-download.com/wp-content/uploads/2018/07/Marvel_logo_red.png'
# offical_mask = np.array(Image.open(requests.get(change_mask, stream=True).raw))

# #Background color
# back_color = '#ffffff'

# #Word cloud format
# word_cloud = WordCloud(width = 300, height = 300, background_color=back_color, stopwords=STOPWORDS, mask=offical_mask).generate(data)

# #Creating coloring from image
# image_colors = ImageColorGenerator(offical_mask)
# plt.figure(figsize=[7,7])
# plt.imshow(word_cloud.recolor(color_func=image_colors), interpolation="bilinear")
# plt.axis("off")
# _=plt.show()

#Customize popup
plt.scatter([x[1] for x in chosen_black_indices], [x[0] for x in chosen_black_indices], color='black', s=1)  
plt.gca().invert_yaxis()  
plt.xticks([])  
plt.yticks([]) 
plt.show()