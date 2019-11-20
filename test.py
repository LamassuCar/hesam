import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#remember to install the conda pillow
image = mpimg.imread("test.jpg")
if len(image) == 0:
    print("imgage not loaded")
else:
    print("Image was loaded!",type(image),image.shape)
    ysize = image.shape[0]
    xsize = image.shape[1]
    print(ysize , xsize)

    #plt.imshow(image)
    #plt.show()
# region_select = np.copy(image)
color_select = np.copy(image)

# bottom_left = [0,750]
# bottom_right= [750, 1386]
# apex = [ysize/2,xsize/2]

red_threshold = 150
green_threshold = 200
blue_threshold = 200
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

thresholds = (image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2])
color_select[thresholds] = [0,0,0]
mpimg.imsave("image2", color_select)
plt.imshow(color_select)
plt.show()

