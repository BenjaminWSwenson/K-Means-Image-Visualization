from PIL import Image
import numpy as np
from sklearn.cluster import KMeans


def read_jpg(filename):
    pic = Image.open(filename)
    image = np.array(pic)
    return image


def get_width_height(image):
    height = len(image)
    width = len(image[0])
    return width, height


def save_jpg(filename, image):
    img = Image.fromarray(image.astype('uint8'))
    img.save(filename)


def assign_clusters(image, k):
    width, height = get_width_height(image)
    arr = np.reshape(image, (width*height, 3))
    k_means = KMeans(n_clusters=k, random_state=0).fit(arr)
    new_image = np.zeros([height, width, 3], dtype=int)
    for i in range(height):
        for j in range(width):
            new_image[i][j] = k_means.cluster_centers_[k_means.predict([image[i][j]])]
    return new_image
